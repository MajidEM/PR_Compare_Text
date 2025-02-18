# The below script will run as part of the github actions in .github/workflows/compare_pr.yml
import re,sys

def pair_items(versions_list):
	'''
	Get the Pairs of the versions.
	'''
	pairs = []
	for i in range(0, len(versions_list), 2):
	    if i + 1 < len(versions_list):
	        pairs.append((versions_list[i], versions_list[i + 1]))
	    else:
	        pairs.append((versions_list[i], None))
	return pairs

def remove_signs_newline(input_str):
	'''
	Tweak the version strings and remove the + and - sign
	'''
	if re.match(r"^\+", input_str):
		output_str = input_str.lstrip("+").strip("\n")
	elif re.match(r"^\-", input_str):
		output_str = input_str.lstrip("-").strip("\n")
	return output_str


def generate_diffs(diff_text):
	'''
	Generate the diffs for the FROM strings.
	'''
	versions_list = []
	fh = open(diff_text, "r")
	lines = fh.readlines()
	for line in lines:
		if re.match(r"^[+-]FROM.*", line):
			versions_list.append(line)
	
	# Handle the first time PR which does not have any differences.
	if len(versions_list) == 1:
		version_str = remove_signs_newline(versions_list[0])
		print ("No diff found for "+version_str)
	
	# Handle the differences in PR.
	elif len(versions_list) > 1:
		pairs = pair_items(versions_list)
		for pair in pairs:
			old_version = remove_signs_newline(pair[0])
			new_version = remove_signs_newline(pair[1])
			if old_version != new_version:
				print ("Diff found for "+new_version+" docker images")
			else:
				print ("No diff found for "+new_version")
	else:
		print ("Don't see any changes in the Dockerfiles submitted in the PR")

diff_text = sys.argv[1]
generate_diffs(diff_text)
