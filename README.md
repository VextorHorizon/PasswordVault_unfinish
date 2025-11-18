# Minimal Password Vault (CLI Version) (Unfinish!)

A simple and beginner-friendly password vault built entirely with Python — designed to demonstrate fundamental concepts like:

- Reading and writing JSON files
- Securely storing multiple passwords
- Basic CLI (Command Line) interaction
- Managing file paths safely with `os.path`

This tool stores password entries in a `vault.json` file using Python's built-in `json` module.  
If the file doesn't exist, it creates a new one and stores your data as key-value pairs like:

```json
{
  "gmail": "password123",
  "github": "supersecurepass"
}
