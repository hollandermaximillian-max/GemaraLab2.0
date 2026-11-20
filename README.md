# Gemara Lab
A static, browser-based learning site. No accounts, points, streaks or server.

## Publish on GitHub Pages
1. Create a public repository (e.g. gemara-lab).
2. Extract the ZIP. Upload all files at its root, including index.html, app.js, data.js and vocabulary.csv. Commit.
3. Settings > Pages > Build and deployment: Deploy from a branch. Select main and / (root), Save.
4. Use the URL shown in Pages when deployment finishes.

## Curriculum maintenance
The bundled data is manually curated and includes Hebrew formulas and illustrative phrases, not a corpus-ranked or fully Jastrow-verified dataset. Levels are provisional. vocabulary.csv is editable in Sheets. IDs must remain unique and stable. Columns: id, level (1–12), category, term, translation, explanation, aliases (semicolon separated). For personal imports, use Settings. For everyone on the hosted site, update vocabulary.csv and regenerate data.js (run update_data.py with Python 3), commit both files. A published Google Sheets CSV feed can be configured in Settings per browser; it is refreshed on opening the site, subject to network access and CORS. Imported rows merge by ID and are not deleted automatically. Adding entries can change lesson groupings; append within levels where practical. Progress is per browser and saved locally; export backups before clearing browser data. Typed answers support exact normalized matching and self-assessment for synonyms. Spaced repetition is a simple interval schedule, not FSRS. Unit tests sample up to 25 entries. The content includes illustrative sentences, not a sourced passage curriculum.

## Local use
Open index.html directly in a browser. No installation needed. For network feeds use the hosted HTTPS site.

## Binyanim update
Replace the six files in your existing GitHub repository. Existing IDs, order and browser storage key are unchanged. Optional CSV columns: binyan, root, verb_form. Binyan practice is under Practice > Mode; it does not change translation mastery. Annotations are provisional and refer to the listed gloss, not every possible reading of an unvocalized form. Unannotated entries are not necessarily non-verbs.

## Vocabulary in context
Upload all files, including context.js. The Context tab provides highlighted-word quizzes, translations, breakdowns, daf links, and separate local review records. Edit context.js to add excerpts. References are manually selected and not independently verified; check the daf before public educational use. Existing storage key and vocabulary IDs are unchanged.
