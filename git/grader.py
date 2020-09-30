#This is a template for the grader

from onpit import Grader
from os.path import join, exists
import git

class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
		if inputCommand == "git clone https://github.com/kwendim/IntroductionToOs.git" or inputCommand == "git clone https://github.com/kwendim/IntroductionToOs":
			return True
		if exists(join(workingDir, 'IntroductionToOs')):
			return self.is_git_repo(join(workingDir, 'IntroductionToOs'))



	@Grader.addStep(name='step2')
	def step2(self, workingDir, inputCommand):
		if exists(join(workingDir, 'IntroductionToOs', 'description.txt')):
			return True

	@Grader.addStep(name='step3')
	def step3(self, workingDir, inputCommand):
		if self.is_git_repo(join(workingDir, 'IntroductionToOs')):
			repo = git.Repo(join(workingDir, 'IntroductionToOs'))
			commit = repo.head.commit
			message = commit.message.strip()
			if message == "add description":
				return True
				
	def is_git_repo(self, path):
		try:
			_ = git.Repo(path).git_dir
			return True
		except git.exc.InvalidGitRepositoryError:
			return False





