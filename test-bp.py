import tempfile

from waldo.jenkins.branch_protect.pr_manager import Manager
from waldo.jenkins.branch_protect.components import PullRequest


with tempfile.TemporaryDirectory() as tmpdir:
  # manager = Manager(
  #   run_dir=tmpdir,
  #   head_branch='andrta31-patch-1',
  #   base_branch='master',
  #   pull_request_number=213
  # )
  # manager.manage()
  pull_request = PullRequest(
    run_dir=tmpdir,
    pull_request_number=213,
    head_branch='andrta31-patch-1',
    base_branch='master',
    list_of_pdk=None
  )
  pull_request.add_reviewers()
