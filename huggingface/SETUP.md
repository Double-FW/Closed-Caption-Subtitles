# Weekly Closed Caption Subtitles updates

Source: https://github.com/Double-FW/Closed-Caption-Subtitles

Destination: https://huggingface.co/datasets/GarethFW/Closed_Caption_Subtitles

The destination is fixed in export-config.json. No HF_DATASET_ID variable is needed.
Save a destination-scoped Hugging Face token as repository secret HF_TOKEN, then
create .github/workflows/huggingface-sync.yml from WORKFLOW_TO_COPY.txt in the
setup download. Run manually once and check the result; weekly runs are Mondays
at 07:23 UTC. Never commit credentials; use the token copy button.

All approved source files are required. Review new or renamed sources in the export
list. The historical RAG remains document-only. CCS identities, human review limits
and unnumbered production/QA context are preserved; no caption tests are executed.
