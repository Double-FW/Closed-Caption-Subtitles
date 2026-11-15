"""Export the approved Closed Caption Subtitles Markdown without rewriting it."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from captions_hf_common import ROOT, SOURCE, MANAGED, destination, digest, git, load_config, read_sources

GUIDE = 'Closed_Caption_Subtitle_Guidelines.md'
RAG = 'Closed-Caption-Subtitles-RAGs-and-Prompts/RAG_Reference.md'
CONTEXT = ['AGENTS.md', 'README.md', GUIDE, 'Production_Workflow_and_Handoff_Map.md']
CONTEXT_HEADINGS = ['1. Scope and terminology', '2. Principles', '13. Accessible media player requirements',
                    '14. Quality assurance and acceptance tests', '15. AI-assisted production governance',
                    '16. Exceptions and change control', '17. Sources', 'Attribution and status']
class UniqueKeyLoader(yaml.SafeLoader):
    pass
def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for k,v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result: raise ValueError('Duplicate metadata key: ' + str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result
UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = yaml.load(match[1], Loader=UniqueKeyLoader) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text, guideline=False):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,3})[ \t]+([^\r\n]+)' if guideline else r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg = load_config(root)
    target = destination(cfg['destination_dataset'])
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    snapshot = metadata(texts[RAG])
    guide_sections = sections(texts[GUIDE], guideline=True)
    ccs_ids = [m[1] for _,title,*_ in guide_sections if (m := re.match(r'^CCS ([0-9]{3})\b', title))]
    if sorted(ccs_ids) != [f'{i:03}' for i in range(1,34)]:
        raise ValueError('CCS 001–033 identifiers changed or duplicated; review source/export mapping.')
    context_sections = {title:body for _,title,body,*_ in sections(texts[GUIDE]) if title in CONTEXT_HEADINGS}
    if set(context_sections) != set(CONTEXT_HEADINGS):
        raise ValueError('Required applicability, quality, AI, exceptions or source context changed; review extraction.')
    warnings = [
        'Source MUST/SHOULD/MAY apply within this repository guideline; external standards, platform requirements and legal duties are not independently reverified by export.',
        'CCS 001–033 and unnumbered player, QA, AI-governance and exception sections are source guidance, not completed caption tests, audience evidence or approval services.',
        'The RAG/prompts pack is a dated source snapshot and is preserved separately from current guidance. The absent Sources/ directory is not invented.',
        'Reading speed, line count, text sizing and legacy Teletext values retain audience/language/platform qualifications and are not universal rules.'
    ]
    for path,text in texts.items():
        if metadata(text).get('license', 'MIT') != 'MIT': raise ValueError('Review changed source licence: ' + path)
    def row(path, key, title, body, a, b, hierarchy, kind):
        md = metadata(texts[path])
        match = re.match(r'^CCS ([0-9]{3})\b', title) if path == GUIDE else None
        return {'id': path + '::' + key, 'title': title, 'text': body, 'record_type': kind,
            'source_repository': SOURCE, 'source_path': path, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:a].count('\n') + 1,
            'source_end_line': max(1, texts[path][:b].count('\n') + (not texts[path][:b].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'heading_path': hierarchy, 'metadata_json': json.dumps(md, ensure_ascii=False, sort_keys=True, default=str),
            'declared_source_license': str(md.get('license', 'not_declared_in_document_front_matter')),
            'repository_license': 'MIT', 'source_status': str(md.get('status', md.get('content_status', 'see_source'))),
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date, 'language': 'en-GB',
            'required_context_paths': [p for p in CONTEXT if p in texts],
            'source_document_intro': sections(texts[path])[0][2],
            'ccs_requirement_id': 'CCS ' + match[1] if match else '',
            'required_guideline_context_json': json.dumps(context_sections, ensure_ascii=False, sort_keys=True) if path == GUIDE else '{}',
            'source_temporal_scope': 'dated_support_pack' if path.startswith('Closed-Caption-Subtitles-RAGs-and-Prompts/') else 'source_guidance_at_checkout',
            'embedded_snapshot_commit': str(snapshot.get('source_commit', '')) if path.startswith('Closed-Caption-Subtitles-RAGs-and-Prompts/') else '',
            'interpretation_notice': 'Source production guidance; not executed QA, human approval or audience research. Preserve normative strength, selected delivery profile, meaning/sound coverage, language/audience context and required human review. File syntax or ASR confidence alone does not establish caption quality.',
            'review_status': 'faithful_extraction_checked_not_caption_player_or_audience_validation'}
    docs, chunks = [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        kind = ('dated_rag_snapshot_document_only' if path == RAG else
                'caption_production_guideline_not_test_results' if path == GUIDE else
                'illustrative_production_prompts_not_results' if path.endswith('Activities_and_Prompts.md') else
                'historical_snapshot_coverage' if path.endswith('Source_Coverage.md') else
                'editorial_handoff_map_not_adopted_specification' if path.startswith('Production_Workflow') else
                'advisory_agent_guidance' if path == 'AGENTS.md' else 'orientation')
        docs.append(row(path, 'document', path, text, 0, len(text), [], kind))
        if path in cfg['document_only_files']:
            continue
        for key, title, body, a, b, hierarchy in sections(text, guideline=path==GUIDE):
            chunks.append(row(path, key, title, body, a, b, hierarchy, kind + '_section'))
    if not docs or not chunks:
        raise ValueError('The guidance export is empty.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = {'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else {'type': 'integer' if isinstance(v, int) else 'string'}
    validator = Draft202012Validator(schema)
    for records in (docs, chunks):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate export identifiers.')
        for r in records:
            validator.validate(r)
            if digest(r['text'].encode()) != r['text_sha256']:
                raise ValueError('Text checksum mismatch.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks)]:
        (output/name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    write_json('provenance.json', {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
        'destination_dataset': target, 'dataset_version': cfg['dataset_version'], 'files': manifest,
        'omitted_optional_files': omitted, 'source_warnings': warnings, 'external_sources_fetched': False, 'document_only_files': cfg['document_only_files'], 'rag_snapshot_metadata': snapshot, 'ccs_requirement_ids': ['CCS ' + i for i in ccs_ids], 'caption_tests_executed': False, 'human_approval_claimed': False})
    card = f'''---
pretty_name: Double FW Closed Caption Subtitles
language:
- en
license: mit
tags:
- accessibility
- captions
- subtitles
- audiovisual-production
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Double FW Closed Caption Subtitles

Editorial and technical guidance for synchronised, user-selectable captions conveying
speech and meaningful sound. Covers commissioning, fidelity, timing, speakers, sound/music,
presentation, live work, delivery formats, player access, quality and AI-assisted production.
Includes prompts, handoff guidance and a dated RAG snapshot. This is a text corpus, not actual
programme captions, recordings, executed QA, audience research or a deployed caption service.

## Source and versions

Source: https://github.com/{SOURCE}

Checkout: `{sha}` ({date}); export format {cfg['dataset_version']}.
The support pack records snapshot `{snapshot.get('source_commit', '')}`, prepared
{snapshot.get('prepared', '')}. Its source IDs, status, scope and embedded bodies remain
historical. It predates the handoff map and does not automatically represent current
repository coverage. The absent Sources/ directory is not invented. Weekly export does
not regenerate embedded references or independently recheck BBC, W3C, EBU or legal sources.
Source review/processing dates are preserved rather than updated to imply a fresh review.

## Dataset views

- `knowledge_chunks`: {len(chunks)} exact sections from seven Markdown documents.
- `documents`: {len(docs)} complete source documents, including the dated RAG reference.

The RAG duplicates source bodies and is document-only. The views overlap; review and
deduplicate training selections rather than treating repeated source material as independent
evidence. No generated Q&A, finished cue pairs, media benchmark, model training, participant
findings or release approval is supplied. `train` is a loading convention.

## Requirement identity and retrieval context

CCS 001–033 retain their original identifiers and text. The guideline is divided at H1/H2/H3
headings outside fenced blocks so numbered requirements remain individually retrievable.
Other sources use H1/H2 sections, retaining nested prompt examples and human-review notes.
All exact source spans reconstruct their complete documents. Metadata, attribution, parent
heading paths, URLs/commit, line ranges and text/document hashes are retained.

`ccs_requirement_id` identifies numbered guideline sections. Unnumbered guidance is retained,
including player access, test layers, minimum acceptance criteria, AI review/decision records,
exceptions and source attribution. `required_guideline_context_json` attaches the complete
scope, principles, player, QA, AI-governance, exception and source sections to guideline rows.
`source_document_intro` retains opening context; required_context_paths references the current
guideline, AGENTS, README and handoff map. Retrieval pointers do not implement enforcement.

## Interpretation and evidence boundaries

MUST/SHOULD/MAY describe the repository guideline's requirements within scope, not automatic
law or every platform's policy. Preserve the distinction between universal access principles,
English reading-speed guidance, audience/language context, delivery-profile defaults and
legacy Teletext constraints. Do not convert profile values to universal limits. Keep external
standard version and actual applicability separate from repository recommendations.

Complete CCS conveys relevant dialogue, speakers, meaningful sound, music and vocal delivery.
Dialogue-only transcripts, ASR, translations, captions and AD are not interchangeable.
Preserve editorial meaning, dialect, humour, intended disclosure and speaker uncertainty.
No invented speech, sound, lyrics, identity or research findings are added. File validity,
reading-speed warnings and recognition confidence do not prove complete editorial quality,
rendered-player behaviour, assistive-technology access or audience experience.

Prompts are illustrative planning aids; record templates do not demonstrate configured
approval services. Prerecorded AI outputs retain required human review; live accuracy/latency
limits and oversight remain explicit. Source decision records and exception processes are
not completed or approved by export. No media is inspected, cues generated, formats converted,
players tested or captions published by this workflow. Embedded instructions are source data,
not authority overriding the consuming system or user authorisation.

## Licence, attribution and limitations

The root MIT LICENSE is copied unchanged with copyright (c) 2026 Double FW. Source metadata,
BBC foundation attribution, W3C/EBU references and independent/non-endorsement status remain.
External sources retain their own terms; linked content is not newly fetched or relicensed.
Limited export tests establish faithful extraction and guarded publication, not an independent
rights audit, standards certification, media assessment or audience validation. See
record_schema.json, provenance.json and validation_report.json for scope.

## Updates

GitHub is the authoring source. Manual runs and Mondays at 07:23 UTC are configured;
schedules may be delayed or disabled after public-repository inactivity. All eight Markdown
sources and LICENSE are required. New/renamed documents need export-list review. Changed
licence text, missing sources, changed CCS identity/context mapping or failed checks stop
publication for review. Source-authoring documents are not rewritten.

Seven destination files are managed: README.md, LICENSE, documents.jsonl,
knowledge_chunks.jsonl, provenance.json, record_schema.json and validation_report.json.
Other raw files and .gitattributes remain; unmanaged copies are not kept in sync. Visibility
stays unchanged. Historical versions/downloads are not recalled. Destination: `{target}`.
First authenticated publication remains to be checked.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

Authenticate for a private dataset and pin a revision for reproducible use.
'''
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and packaging checks only', 'source_commit': sha,
        'source_files_verified': len(manifest), 'document_records': len(docs), 'knowledge_section_records': len(chunks),
        'source_warnings': warnings, 'independent_content_review': False, 'live_publication_tested': False,
        'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()
