# Local security configuration

This review branch removes the identified hardcoded server configuration from the modified files. The default branch remains unchanged pending verification.

## Setup

Supply the variables in .env.example through the shell or deployment environment. The application does not automatically load a .env file. Never commit real values. Use a least-privilege Supabase key appropriate to the server operation, verify RLS, and do not reuse a browser key as an administrative credential.

Generate a new random FLASK_SECRET_KEY locally; replacing it invalidates existing session cookies. Run from the flask directory after configuring the variables.

## Required before merge

1. Review the project's other credential references and rotate any exposed secret or privileged key through the provider. Do not assume every public Supabase publishable/anon key is secret; verify its role and policies.
2. Configure the test environment and run the existing app; verify login, database reads/writes and relevant authorization rules.
3. Review previous Git commits and external copies. Removing a literal from the current file does not revoke it or remove it from history.
4. Ignore patterns prevent new generated files from being added; the tracked paths removed in this branch are listed below.

No credential values are included in this guide. No live keys were tested or revoked.

## Tracked build artifacts

The review branch also removes the following generated paths from the Git tree:

- `flask/.vs`
- `flask/__pycache__`
- `flask/views/__pycache__`

Python recreates bytecode caches when required.
Historical Git objects remain unchanged. The application source, project data, and research artifacts are preserved.
