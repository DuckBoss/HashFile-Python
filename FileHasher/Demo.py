import HashFile
import sys
import datetime as dt

def main():
	# Start a timer to see how long it takes to execute
	start = dt.datetime.now()

	# Initialize Hashing Class in HashFile
	program = HashFile.Hashing()
	# Get MD5 Hash from CL-Arguments
	md5Return = program.HashFileIntoMD5(sys.argv[1])
	# Get SHA1 Hash from CL-Arguments
	sha1Return = program.HashFileIntoSHA1(sys.argv[1])

	end = dt.datetime.now()

	# Print out results of hashing
	print("MD5 Result: {}".format(md5Return))
	print("SHA1 Result: {}".format(sha1Return))
	print("Total Execution Time: {}".format(end-start))

if __name__ == "__main__":
	main()