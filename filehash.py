import sublime
import sublime_plugin
import hashlib

# generate a hash for a document and insert it

class AddHashToColdfusionFile(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        fileType = view.file_name()[-4:]
        if (not fileType == ".cfm") and (not fileType == ".cfc"):
                return

        edit = view.begin_edit()
        # find all the existing hashes in the document
        hashes = view.find_all("<!--- MD5 ([a-z0-9]+) --->", 0)
        for hashRegion in reversed(hashes):
            view.replace(edit, hashRegion, "<!--- MD5 --->")

        # generate a hash of the document
        fileContents = view.substr(sublime.Region(0, view.size()))

        m = hashlib.md5()
        m.update(fileContents)
        hashText = m.hexdigest()

        # now find the places to insert the hash
        hashes = view.find_all("<!--- MD5 --->", 0)

        for hashRegion in reversed(hashes):
                view.replace(edit, hashRegion,
                        "<!--- MD5 {0} --->".format(hashText))

        view.end_edit(edit)
