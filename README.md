# Sublime Insert Hash Plugin

When a file is saved the MD5 hash of the file's contents is inserted at identifiable points.
Currently only coldfusion comments are supported points of insertion.

    <!--- MD5 --->

Before the hash is calculated any previous entries are removed. This means that the hash will
not match a hash which generated externally, but can be used to compare files before and after.
The contextual search is not very smart, so it can be used to insert hashes into variables.

    <cfset request.version = "<!--- MD5 --->">

## To Do

- Add support for more languages.
- Improve comment searching, so that only comment scopes are searched for the substitution strings.