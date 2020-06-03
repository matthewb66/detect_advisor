# Synopsys Detect Advisor Script - detect_advisor.py
# OVERVIEW

This script is provided under an OSS license (specified in the LICENSE file) to assist users when scanning projects using the Synopsys Detect program to scan projects.

It does not represent any extension of licensed functionality of Synopsys software itself and is provided as-is, without warranty or liability.

# DESCRIPTION

The `detect_advisor.py` script is designed to pre-scan a project folder to determine whether the Synopsys Detect program (see https://blackducksoftware.github.io/synopsys-detect/latest/) used for Synopsys Black Duck SCA scans can be executed (the prerequisites are met) and also to provide recommendations and advice on how to perform and optimize scanning.

It is available as a python script with no prerequisites except Python 3 (can be downloaded and run without dependencies), or alternatively compiled executables for Windows, Linux and Mac OS are provided in the `executables` folder for download and execution standalone.

The script will check the prerequisites to run Detect (including the correct version of Java) and scan the project location for files and archives, calculate the total scan size, check for project (package manager) files and package managers themselves and will also detect large duplicate files and folders.

It will expand .zip and .jar files automatically, processing recursive files (zips within zips etc.). Other archive types (.gz, .tar, .Z etc.) are not currently expanded by detect_advisor (although they will be expanded by Synopsys Detect).

It will produce a set of categorized recommendations and Detect command line options to support different types of scans and other operations.

It can optionally write a report file including the console output and other information. It can also create a set of `.bdignore` files (to ignore duplicate folders or those containing only binary files) in sub-folders as well as a .yml project config file containing relevant, commented-out Detect options which can be uncommented, and the .yml can be referenced using the Synopsys Detect option `--spring.profiles.active=project`.

Optionslly, only critical issues (which will stop Detect from scanning at all) can be reported to the console.

An interactive mode is available which will ask a series of questions about the options to use for the advisor analysis.

# PREREQUISITES

Python 3 must be installed prior to using this script. Alternatively, compiled, standalone executables are available for Windows, Linux and Mac OS in the `executables` folder.

# USAGE

The `detect_advisor.py` script can be invoked as follows:

    usage: detect_advisor [-h] [-r REPORT] [-d] [-s] [-c] [-o] [-D] [-b] [scanfolder]

    Examine files/folders to determine scan recommendations

    optional arguments:
      scanfolder             Top level folder to analyse
      -h, --help             show this help message and exit
      -i, --interactive      Ask questions to confirm required options (will be used if 'scanfolder' is blank)
      -r REPORT, --report REPORT
                             Output report file (existing report files will be renamed)
      -d, --dependency_only  Check for detector (package manager) files and prerequisites only - for dependency scans
      -s, --signature_only   Check for files and folders for signature scan only
      -c, --critical_only    Only show critical issues which will cause Detect to fail
      -o, --output_config    Create .yml config and .bdignore file in project folder
      -b, --bdignore         Create multiple .bdignore files in sub-folders to ignore duplicate folders
      -D, --docker           Check for docker prerequisites
      --docker_only          Check for docker prerequisites only

If `scanfolder` is not specified then options will be requested interactively (alternatively use `-i` or `--interactive` option to specify interactive mode). Enter q or use CTRL-C to terminate interactive entry and the program.

When specified, `scanfolder` can be a relative or absolute path (special characters such as ~ or environment variables such as $HOME are not supported in interactive mode).

The `-r repfile` or `--report repfile` option will output the console messages and additional information to the file `repfile`, moving previous repfile if it exists to `repfile.XXX` where XXX is an incremental number.

The `-c` or `--critical_only` option will limit the console output to critical issues only, skipping the summary section and other information, although all sections will still be written to the report file (if specified with `-r repfile`).

The `-d` and `-s` options specify that ONLY Dependency (Detector) or Signature scan checking should be performed respectively.

The `-o` or `--output_config` option will create an `application-project.yml` in the project folder with commented out Detect parameters. Uncomment the required parameters and then specify the Detect option `--spring.profiles.active=project` to use this profile.

The `-D` or `--docker` option will check docker scanning prerequisites in addition to other checks; use `--docker_only` to check only docker prerequisites (other checks not performed).

# EXAMPLE USAGE

The following command will allow options to be entered interactively:

    python3 detect_advisor.py
    
The interactive questions are shown below:

    Enter project folder to scan (default current folder '/Users/myuser/myproject'):
    Types of scan to check? (b)oth, (d)ependency or (s)ignature] [b]:
    Docker scan check? (y/n) [n]:
    Critical recommendations only? (y/n) [n]:
    Create output report file? (y/n) [y]:
    Report file name [report.txt]:
    Create .bdignore files (y/n) [n]:
    Create application-project.yml file? (y/n) [n]:

The following command will run the script on the `myproject` sub-folder, producing standard console output only:

    python3 detect_advisor.py myproject
    
The following command will run the script on the `myproject` sub-folder, producing standard console output and outputting additional information to the `myreport.txt` file (if myreport.txt already exists it is renamed to myreport.001 and so on):

    python3 detect_advisor.py -r myreport.txt myproject

The following command will scan the absolute path `/users/matthew/myproject`; the `-c` option will reduce the console output to only include critical issues while writing full output in the `myreport.txt` file:

    python3 detect_advisor.py -c -r myreport.txt /users/myuser/myproject
    
The following command will scan the absolute path `/users/myuser/myproject`; the `-o` option will cause the `application-project.yml` file to be written to the /users/myuser/myproject folder:

    python3 detect_advisor.py -o /users/myuser/myproject

The following command will scan the absolute path `/users/myuser/myproject`; the `-b` option will cause multiple .bdignore files to be created in relevant sub-folders to ignore large duplicate folders or folders containing only binary files. USE WITH CAUTION as it will cause specified folders to be permanently ignored by the Signature scan (until the .bdignore files are removed):

    python3 detect_advisor.py -b /users/myuser/myproject

The following command will scan the absolute path `/users/myuser/myproject` and output to the myreport.txt file; the `-s` option will cause only Signature scan checking to be performed:

    python3 detect_advisor.py -s -r myreport.txt /users/myuser/myproject

The following command will scan the absolute path `/users/myuser/myproject`; the `-D` option will also check Docker scanning prerequisites:

    python3 detect_advisor.py -D /users/myuser/myproject

# SUMMARY INFO

This section includes counts and size analysis for the files and folders beneath the project location.

The `Size Outside Archives` value in the `ALL FILES (Scan Size)` row represents the total scan size as calculated by Detect (used for capacity license).

Note that the `Archives(exc. Jars)` row covers all archive file types but that only .zip files are extracted by `detect_advisor` (whereas Synopsys Detect extracts other types of archives automatically). The final 3 `Inside Archives` columns indicate items found within .zip archives for the different types (except for the Jar row which references .jar/.ear/.war files). The `Inside Archives` columns for the Archives row itself reports archive files within .zips (or nested deeper - zips within zips within zips etc.).

    SUMMARY INFO:
    Total Scan Size = 5,856 MB

                             Num Outside     Size Outside      Num Inside     Size Inside     Size Inside
                                Archives         Archives        Archives        Archives        Archives
                                                            (UNcompressed)    (compressed)
    ====================  ==============   ==============   =============   =============   =============
    Files (exc. Archives)        297,415         4,905 MB         130,126          653 MB          160 MB
    Archives (exc. Jars)              39           951 MB               9            0 MB            0 MB
    ====================  ==============   ==============   =============   =============   =============
    ALL FILES (Scan size)        297,454         5,856 MB         130,135          654 MB          160 MB
    ====================  ==============   ==============   =============   =============   =============
    Folders                       30,435              N/A          10,309             N/A             N/A   
    Ignored Folders                4,169         2,319 MB               0            0 MB            0 MB
    Source Files                 164,240         1,024 MB          53,740          171 MB           34 MB
    JAR Archives                       6             6 MB               0            0 MB            0 MB
    Binary Files                      33            99 MB              10            0 MB            0 MB
    Other Files                  129,476         2,988 MB          75,282          478 MB          124 MB
    Package Mgr Files              3,633            25 MB           1,094            2 MB            0 MB
    OS Package Files                   0             0 MB               0            0 MB            0 MB
    --------------------  --------------   --------------   -------------   -------------   -------------
    Large Files (>5MB)                38           336 MB               1            9 MB            4 MB
    Huge Files (>20MB)                27         1,875 MB               1           35 MB            6 MB
    --------------------  --------------   --------------   -------------   -------------   -------------

    PACKAGE MANAGER CONFIG FILES:
    - In invocation folder:   0
    - In sub-folders:         3633
    - In archives:            0
    - Minimum folder depth:   2
    - Maximum folder depth:   14
    ---------------------------------
    - Total discovered:       3633

    Config files for the following Package Managers found: gradlew, gradle, clang, dotnet, npm, yarn, pod, python, python3, pip

# RECOMMENDATIONS

This section includes a list of findings categorised into CRITICAL (will cause Detect to fail), IMPORTANT (may impact the scope and type of scan) and INFORMATION (potential additional options depending on requirements but which will not impact scope of the standard scan):

    RECOMMENDATIONS:
    - CRITICAL: Overall scan size (6,520 MB) is too large
        Impact:  Scan will fail
        Action:  Ignore folders or remove large files

    -----------------------------------------------------------------------------------------------------    
    - IMPORTANT: No package manager files found in invocation folder but do exist in sub-folders
        Impact:  Dependency scan will not be run
        Action:  Specify --detect.detector.depth=5
        
    - IMPORTANT: Package manager programs (dotnet) missing for package files in sub-folders
        Impact:  The scan will fail if the scan depth is modified from the default
        Action:  Either install package manager programs or
                 consider specifying --detect.detector.buildless=true
                 
    - IMPORTANT: Large amount of data (396 MB) in 66 binary files found
        Impact:  Binary files not analysed by standard scan, will impact Capacity license usage
        Action:  Remove files or ignore folders, also consider zipping
                 binary files and using Binary scan
                 
    - IMPORTANT: Large amount of data (594 MB) in 8 duplicate folders
        Impact:  Scan capacity potentially utilised without detecting additional
                 components, will impact Capacity license usage
        Action:  Remove or ignore duplicate folders
        
    - IMPORTANT: Large amount of data (556 MB) in 17 duplicate files
        Impact:  Scan capacity potentially utilised without detecting additional
                 components, will impact Capacity license usage
        Action:  Remove duplicate files or ignore folders
    
    -----------------------------------------------------------------------------------------------------    
    - INFORMATION: Overall number of files (653,981,695) is large
        Impact:  Scan time could be long
        Action:  Ignore folders or split project (scan sub-projects)
        
    - INFORMATION: License or notices files found
        Impact:  Local license text may need to be scanned
        Action:  Add options --detect.blackduck.signature.scanner.license.search=true
                 and optionally --detect.blackduck.signature.scanner.upload.source.mode=true

    - INFORMATION: Source files found for which Snippet analysis supported
        Impact:  Snippet analysis can discover copied OSS source files and functions
        Action:  Add options --detect.blackduck.signature.scanner.snippet.matching=SNIPPET_MATCHING

    - INFORMATION: 5739 singleton .js files found
        Impact:  OSS components within JS files may not be detected
        Action:  Consider specifying Single file matching
                 (--detect.blackduck.signature.scanner.individual.file.matching=SOURCE)

# DETECT CLI

This section includes recommended CLI options for Synopsys Detect. If connectivity to the download locations is not verified by detect_advisor, then proxy options will also be added in case a proxy connection is required.

    DETECT CLI:
    
        DETECT COMMAND:
        bash <(curl -s -L https://detect.synopsys.com/detect.sh)
    
        MINIMUM REQUIRED OPTIONS:
            --blackduck.url=https://YOURSERVER
            --blackduck.api.token=YOURTOKEN
            --detect.source.path='/Users/myuser/myproject'
            --detect.detector.buildless=true
                (OR install package managers 'dotnet' OR use --detect.XXXX.path=<LOCATION>
                where XXX is package manager)

            (Note that .bdignore exclude file is recommended - see the report file 'repfile.txt' or use '-o' option)


        OPTIONS TO IMPROVE SCAN COVERAGE:
            --detect.detector.depth=2
                (To find package manager files within sub-folders; note depth 2 would find
                all PM files in sub-folders but higher level projects may already include them
            --detect.binary.scan.file.path=binary_files.zip
                (To scan binary files within the project; zip files first - see list of binary
                files in report file; binary scan license required)
            --detect.blackduck.signature.scanner.individual.file.matching=SOURCE
                (To check singleton .js files for OSS matches)


        OPTIONS TO OPTIMIZE DEPENDENCY SCAN:
             For dotnet:
            --detect.nuget.config.path=PATH
                (OPTIONAL The path to the Nuget.Config file to supply to the nuget exe)
            --detect.nuget.packages.repo.url=URL
                (OPTIONAL Nuget Packages Repository URL (default: https://api.nuget.org/v3/index.json).)
            --detect.nuget.excluded.modules=PROJECT
                (OPTIONAL Nuget Projects Excluded: The names of the projects in a solution to exclude.)
            --detect.nuget.ignore.failure=true
                (OPTIONAL Ignore Nuget Failures: If true errors will be logged and then ignored.)
            --detect.nuget.included.modules=PROJECT
                (OPTIONAL Nuget Modules Included: The names of the projects in a solution to include (overrides exclude).)


        PROJECT OPTIONS:
            --detect.project.name=PROJECT_NAME
            --detect.project.version.name=VERSION_NAME
                (Optionally specify project and version names)
            --detect.project.tier=X
                (Optionally define project tier numeric)
            --detect.project.version.phase=ARCHIVED/DEPRECATED/DEVELOPMENT/PLANNING/PRERELEASE/RELEASED
                (Optionally specify project phase - default DEVELOPMENT)
            --detect.project.version.distribution=EXTERNAL/SAAS/INTERNAL/OPENSOURCE
                (Optionally specify version distribution - default EXTERNAL)


    Further information in output report file 'repfile.txt'

# REPORT FILE

An optional report file can be specified (`-r repfile` or `--report repfile`) which will include full information with lists of duplicate large files, duplicate large folders, binary files etc. If the report file already exists it will be backed up to `repfile.XXX` where XXX is an incremental numeric.

If large duplicate files or folders are identified (or folders containing only binary files), then a list of folders to ignore is also produced in the report file.

The report file will also include a list of large binary files, with instructions on how to zip the files and submit for binary scan (note this a separate licensed product to standard Black Duck).

Note that reported paths which include the characters `##` indicate items within zip or similar archives.

# OUTPUT CONFIG FILES

The `-o` or `--output_config` option will create the `application-project.yml` files in the project folder if it does not already exist. The `application-project.yml` file will contain a list of commented Detect options from the DETECT CLI section, which you will need to modify and uncomment according to your needs. The `application-project.yml` config file can be used to configure Detect using the single `--spring.profiles.active=project` option.

The `-b` or `--bdignore` option will create multiple `.bdignore` files in sub-folders beneath the project folder if they do not already exist. The `.bdignore` files will be created in parent folders of duplicate folders or those containing only binary files for exclusion. USE WITH CAUTION as it will cause specified folders to be permanently ignored by the Signature scan until the .bdignore files are removed.
