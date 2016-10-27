import os, re, sublime, sublime_plugin

DEBUG = True

class DebugUtils:
  @staticmethod
  def log(tag, message):
    print (tag + ':' +message);

class FileUtils:
  @staticmethod
  def openFile(view, filepath):
    fileContent = ""
    try:
      fh = open(filepath, 'r', encoding='utf-8')
    except Exception as e:
      #sublime.status_message(e)
      raise e
    else:
      fileContent = fh.read();
      fh.close()
    return fileContent

class SourceCodeGeneratorCommand(sublime_plugin.TextCommand):
	def run(self, edit, filepath=None):
		DebugUtils.log('i', "START")
		DebugUtils.log('i', "filepath:" + filepath)

		currPath = os.path.dirname(os.path.abspath(__file__))
		DebugUtils.log('i', "currPath:" + currPath)
		filepath = currPath + filepath
		fileContent = FileUtils.openFile(self.view, filepath)

		self.view.insert(edit, self.view.sel()[0].begin(), fileContent)

		DebugUtils.log('i', filepath+"'s content was inserted.")
		DebugUtils.log('i', "END")
