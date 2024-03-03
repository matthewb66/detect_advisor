#
# Constants
advisor_version = "0.9 Beta"
detect_version = "9.3.0"

ext_list = {
    'src': ['.4th', '.actionscript', '.ada', '.adb', '.ads', '.aidl', '.as', '.as8', '.asm', '.asp', '.aspx', '.aug',
            '.awk', '.bas', '.bash', '.bat', '.bf', '.bfpp', '.bi', '.bms', '.bmx', '.boo', '.c', '.c#', '.c++',
            '.cbl', '.cc', '.cfc', '.cfm', '.cgi', '.chai', '.clj', '.cljc', '.cljs', '.cls', '.cmd', '.com', '.cpp',
            '.cpy', '.cs', '.cu', '.cuh', '.cxx', '.d', '.dpk', '.dylan', '.e', '.ec', '.eh', '.el', '.erl', '.es',
            '.exec', '.exheres-0', '.exlib', '.f', '.f77', '.f90', '.factor', '.for', '.fpp', '.fr', '.frag', '.frm',
            '.frx', '.fs', '.g77', '.g90', '.glsl', '.go', '.groovy', '.gs', '.h', '.h++', '.haml', '.hh', '.hpp',
            '.hrl', '.hs', '.hx', '.hxx', '.i', '.i3', '.idl', '.inc', '.java', '.js', '.jsp', '.jws', '.l',
            '.lhs', '.lisp', '.lsp', '.lua', '.m', '.m2', '.m3', '.m4', '.ml', '.mli', '.mm', '.mod', '.nb', '.nbs',
            '.octave', '.pas', '.php', '.php3', '.php4', '.php5', '.phps', '.phtml', '.pl', '.pm', '.pp', '.py', '.r',
            '.r3', '.rb', '.rc', '.reb', '.rebol', '.rexx', '.ru', '.s', '.sc', '.scala', '.scm', '.sh', '.sqb',
            '.sql', '.ss', '.st', '.swift', '.tcl', '.tk', '.v', '.vb', '.vba', '.vbe', '.vbs', '.vert', '.vhd',
            '.vhdl', '.vim', '.y', '.z80'],
    'bin': ['.dll', '.obj', '.o', '.a', '.lib', '.iso', '.qcow2', '.vmdk', '.vdi',
            '.ova', '.nbi', '.vib', '.exe', '.img', '.bin', '.apk', '.aac', '.ipa', '.msi'],
    'arc': ['.zip', '.gz', '.tar', '.xz', '.lz', '.bz2', '.7z', '.rar', '.rar',
            '.cpio', '.Z', '.lz4', '.lha', '.arj'],
    'jar': ['.jar', '.ear', '.war'],
    'zip': ['.jar', '.ear', '.war', '.zip'],
    'pkg': ['.rpm', '.deb', '.dmg', '.pki'],
    'lic': ['LICENSE', 'LICENSE.txt', 'notice.txt', 'license.txt', 'license.html', 'NOTICE', 'NOTICE.txt']
}

detectors_file_dict = {
    'build.env': ['bitbake'],
    'cargo.toml': ['cargo'],
    'cargo.lock': ['cargo'],
    'Cartfile': ['carthage'],
    'Cartfile.resolved': ['carthage'],
    'conanfile.txt': ['conan'],
    'conan.lock': ['conan'],
    'pubspec.yaml': ['dart'],
    'pubspec.lock': ['dart'],
    'compile_commands.json': ['clang'],
    'Podfile.lock': ['pod'],
    'environment.yml': ['conda'],
    'Makefile.PL': ['cpan'],
    'packrat.lock': ['rtools'],
    'Gopkg.lock': ['go'],
    'gogradle.lock': ['go'],
    'go.mod': ['go'],
    'vendor.json': ['go'],
    'vendor.conf': ['go'],
    'build.gradle': ['gradlew', 'gradle'],
    'build.gradle.kts': ['gradlew', 'gradle'],
    'ivy.xml': ['ivy'],
    'build.xml': ['ivy'],
    'lerna.json': ['lerna'],
    'rebar.config': ['rebar3'],
    'pom.xml': ['mvnw', 'mvn'],
    'pom.groovy': ['mvnw', 'mvn'],
    'node_modules': ['npm'],
    'package.json': ['npm'],
    'package-lock.json': ['npm'],
    'npm-shrinkwrap.json': ['npm'],
    'composer.lock': ['composer'],
    'composer.json': ['composer'],
    'Package.swift': ['swift'],
    'Package.resolved': ['swift', 'xcode'],
    'package.xml': ['pear'],
    'pipfile': ['python', 'python3', 'pipenv'],
    'pipfile.lock': ['python', 'python3', 'pipenv'],
    'pnpm-lock.yaml': ['pnpm'],
    'pyproject.toml': ['poetry'],
    'setup.py': ['python', 'python3', 'pip'],
    'requirements.txt': ['python', 'python3', 'pip'],
    'Gemfile.lock': ['gem'],
    'build.sbt': ['sbt'],
    'yarn.lock': ['yarn'],
    'Makefile': ['cpp'],
    'makefile': ['cpp'],
    'GNUmakefile': ['cpp'],
    'recipe-depends.dot': ['bitbake'],
    'task-depends.dot': ['bitbake']
}

detectors_ext_dict = {
    '.csproj': ['dotnet'],
    '.fsproj': ['dotnet'],
    '.vbproj': ['dotnet'],
    '.asaproj': ['dotnet'],
    '.dcproj': ['dotnet'],
    '.shproj': ['dotnet'],
    '.ccproj': ['dotnet'],
    '.sfproj': ['dotnet'],
    '.njsproj': ['dotnet'],
    '.vcxproj': ['dotnet'],
    '.vcproj': ['dotnet'],
    '.xproj': ['dotnet'],
    '.pyproj': ['dotnet'],
    '.hiveproj': ['dotnet'],
    '.pigproj': ['dotnet'],
    '.jsproj': ['dotnet'],
    '.usqlproj': ['dotnet'],
    '.deployproj': ['dotnet'],
    '.msbuildproj': ['dotnet'],
    '.sqlproj': ['dotnet'],
    '.dbproj': ['dotnet'],
    '.rproj': ['dotnet'],
    '.sln': ['dotnet'],
    '.mk': ['cpp'],
    '.xcworkspace': ['xcode'],
    '.xcodeproj': ['xcode']
}

detector_cli_options_dict = {
    'bazel':
        "--detect.bazel.cquery.options='OPTION1,OPTION2'\n" +
        "    (OPTIONAL List of additional options to pass to the bazel cquery command.)\n" +
        "--detect.bazel.dependency.type=MAVEN_JAR/MAVEN_INSTALL/UNSPECIFIED\n" +
        "    (OPTIONAL Bazel workspace external dependency rule: The Bazel workspace rule used to pull in external dependencies.\n" + \
        "    If not set, Detect will attempt to determine the rule from the contents of the WORKSPACE file (default: UNSPECIFIED).)\n",
    'bitbake':
        "--detect.bitbake.package.names='PACKAGE1,PACKAGE2'\n" + \
        "    (OPTIONAL List of package names from which dependencies are extracted.)\n" + \
        "--detect.bitbake.search.depth=X\n" + \
        "    (OPTIONAL The depth at which Detect will search for the recipe-depends.dot or package-depends.dot files (default: 1).)\n" + \
        "--detect.bitbake.source.arguments='ARG1,ARG2,ARG3'\n" + \
        "    (OPTIONAL List of arguments to supply when sourcing the build environment init script)\n",
    'clang':
        "    Note that Detect supports reading a compile_commands.json file generated by cmake.\n" + \
        "    If the project does not use cmake then it is possible to produce the compile_commands.json\n" + \
        "    from standard make using utilities such as https://github.com/rizsotto/Bear. Detect must be\n" + \
        "    run on Linux only for the detection of OSS packages using compile_commands.json, and the packages\n" + \
        "    must be installed in the OS.\n",
    'conda':
        "--detect.conda.environment.name=NAME\n" + \
        "    (OPTIONAL The name of the anaconda environment used by your project)\n",
    'cpp':
        "    C/C++ projects built using a compiler should be scanned using the blackduck_c_cpp utility.\n" + \
        "    See https://pypi.org/project/blackduck-c-cpp.\n",
    'dotnet':
        "--detect.nuget.config.path=PATH\n" + \
        "    (OPTIONAL The path to the Nuget.Config file to supply to the nuget exe)\n" + \
        "--detect.nuget.packages.repo.url=URL\n" + \
        "    (OPTIONAL Nuget Packages Repository URL (default: https://api.nuget.org/v3/index.json).)\n" + \
        "--detect.nuget.excluded.modules=PROJECT\n" + \
        "    (OPTIONAL Nuget Projects Excluded: The names of the projects in a solution to exclude.)\n" + \
        "--detect.nuget.ignore.failure=true\n" + \
        "    (OPTIONAL Ignore Nuget Failures: If true errors will be logged and then ignored.)\n" + \
        "--detect.nuget.included.modules=PROJECT\n" + \
        "    (OPTIONAL Nuget Modules Included: The names of the projects in a solution to include (overrides exclude).)\n",
    'gradle':
        "--detect.gradle.build.command='ARGUMENT1 ARGUMENT2'\n" + \
        "    (OPTIONAL Gradle Build Command: Gradle command line arguments to add to the mvn/mvnw command line.)\n" + \
        "--detect.gradle.excluded.configurations='CONFIG1,CONFIG2'\n" + \
        "    (OPTIONAL Gradle Exclude Configurations: List of Gradle configurations to exclude.)\n" + \
        "--detect.gradle.excluded.projects='PROJECT1,PROJECT2'\n" + \
        "    (OPTIONAL Gradle Exclude Projects: List of Gradle sub-projects to exclude.)\n" + \
        "--detect.gradle.included.configurations='CONFIG1,CONFIG2'\n" + \
        "    (OPTIONAL Gradle Include Configurations: List of Gradle configurations to include.)\n" + \
        "--detect.gradle.included.projects='PROJECT1,PROJECT2'\n" + \
        "    (OPTIONAL Gradle Include Projects: List of Gradle sub-projects to include.)\n",
    'mvn':
        "--detect.maven.build.command='ARGUMENT1 ARGUMENT2'\n" + \
        "    (OPTIONAL Maven Build Command: Maven command line arguments to add to the mvn/mvnw command line.)\n" + \
        "--detect.maven.excluded.scopes='SCOPE1,SCOPE2'\n" + \
        "    (OPTIONAL Dependency Scope Excluded: List of Maven scopes. Output will be limited to dependencies outside these scopes (overrides include).)\n" + \
        "--detect.maven.included.scopes='SCOPE1,SCOPE2'\n" + \
        "    (OPTIONAL Dependency Scope Included: List of Maven scopes. Output will be limited to dependencies within these scopes (overridden by exclude).)\n" + \
        "--detect.maven.excluded.modules='MODULE1,MODULE2'\n" + \
        "    (OPTIONAL Maven Modules Excluded: List of Maven modules (sub-projects) to exclude.)\n" + \
        "--detect.maven.included.modules='MODULE1,MODULE2'\n" + \
        "    (OPTIONAL Maven Modules Included: List of Maven modules (sub-projects) to include.)\n" + \
        "--detect.maven.include.plugins=true\n" + \
        "    (OPTIONAL Maven Include Plugins: Whether or not detect will include the plugins section when parsing a pom.xml.)\n",
    'npm':
        "--detect.npm.arguments='ARG1 ARG2'\n" + \
        "    (OPTIONAL Additional arguments to add to the npm command line when running Detect against an NPM project.)\n" + \
        "--detect.npm.include.dev.dependencies=false\n" + \
        "    (OPTIONAL Include NPM Development Dependencies: Set this value to false if you would like to exclude your dev dependencies.)\n",
    'packagist':
        "--detect.packagist.include.dev.dependencies=false\n" + \
        "    (OPTIONAL Include Packagist Development Dependencies: Set this value to false if you would like to exclude your dev requires dependencies.)\n",
    'pear':
        "--detect.pear.only.required.deps=true\n" + \
        "    (OPTIONAL Include Only Required Pear Dependencies: Set to true if you would like to include only required packages.)\n",
    'python':
        "--detect.pip.only.project.tree=true\n" + \
        "    (OPTIONAL PIP Include Only Project Tree: By default, pipenv includes all dependencies found in the graph. Set to true to only\n" + \
        "    include dependencies found underneath the dependency that matches the provided pip project and version name.)\n" + \
        "--detect.pip.project.name=NAME\n" + \
        "    (OPTIONAL PIP Project Name: The name of your PIP project, to be used if your project's name cannot be correctly inferred from its setup.py file.)\n" + \
        "--detect.pip.project.version.name=VERSION\n" + \
        "    (OPTIONAL PIP Project Version Name: The version of your PIP project, to be used if your project's version name\n" + \
        "    cannot be correctly inferred from its setup.py file.)\n" + \
        "--detect.pip.requirements.path='PATH1,PATH2'\n" + \
        "    (OPTIONAL PIP Requirements Path: List of paths to requirements.txt files.)\n",
    'ruby':
        "--detect.ruby.include.dev.dependencies=true\n" + \
        "    (OPTIONAL Ruby Development Dependencies: If set to true, development dependencies will be included when parsing *.gemspec files.)\n" + \
        "--detect.ruby.include.runtime.dependencies=false\n" + \
        "    (OPTIONAL Ruby Runtime Dependencies: If set to false, runtime dependencies will not be included when parsing *.gemspec files.)\n",
    'sbt':
        "--detect.sbt.report.search.depth\n" + \
        "    (OPTIONAL SBT Report Search Depth: Depth the sbt detector will use to search for report files (default 3))\n" + \
        "--detect.sbt.excluded.configurations='CONFIG'\n" + \
        "    (OPTIONAL SBT Configurations Excluded: The names of the sbt configurations to exclude.)\n" + \
        "--detect.sbt.included.configurations='CONFIG'\n" + \
        "    (OPTIONAL SBT Configurations Included: The names of the sbt configurations to include.)\n",
    'yarn':
        "--detect.yarn.prod.only=true\n" + \
        "    (OPTIONAL Include Yarn Production Dependencies Only: Set this to true to only scan production dependencies.)\n"
}

detector_cli_required_dict = {
    'bazel':
        "--detect.bazel.target='TARGET'\n" + \
        "    (REQUIRED Bazel Target: The Bazel target (for example, //foo:foolib) for which dependencies are collected.)\n",
    'bitbake':
        "--detect.bitbake.build.env.name=NAME\n" + \
        "    (REQUIRED BitBake Init Script Name: The name of the build environment init script (default: oe-init-build-env).)\n"
}

linux_only_detectors = ['clang', 'bitbake']

largesize = 5000000
hugesize = 20000000

notinarc = 0
inarc = 1
inarcunc = 1
inarccomp = 2

#
# Variables
max_arc_depth = 0

counts = {
    'file': [0, 0],
    'dir': [0, 0],
    'ignoredir': [0, 0],
    'arc': [0, 0],
    'bin': [0, 0],
    'jar': [0, 0],
    'src': [0, 0],
    'det': [0, 0],
    'large': [0, 0],
    'huge': [0, 0],
    'other': [0, 0],
    'lic': [0, 0],
    'pkg': [0, 0]
}

sizes = {
    'file': [0, 0, 0],
    'dir': [0, 0, 0],
    'ignoredir': [0, 0, 0],
    'arc': [0, 0, 0],
    'bin': [0, 0, 0],
    'jar': [0, 0, 0],
    'src': [0, 0, 0],
    'det': [0, 0, 0],
    'large': [0, 0, 0],
    'huge': [0, 0, 0],
    'other': [0, 0, 0],
    'pkg': [0, 0, 0]
}

file_list = {
    'src': [],
    'bin': [],
    'large': [],
    'huge': [],
    'arc': [],
    'jar': [],
    'other': [],
    'pkg': []
}

bin_large_dict = {}

# bdignore_list = []

det_dict = {}
detectors_list = []

crc_dict = {}

dup_dir_dict = {}
dup_large_dict = {}

dir_dict = {}
large_dict = {}
arc_files_dict = {}

messages = ""
recs_msgs_dict = {
    'crit': '',
    'imp': '',
    'info': ''
}
cli_msgs_dict = {
    'reqd': "--blackduck.url=https://YOURSERVER\n" + \
             "--blackduck.api.token=YOURTOKEN\n", 'proj': "--detect.project.name=PROJECT_NAME\n" + \
                                                          "--detect.project.version.name=VERSION_NAME\n" + \
                                                          "    (OPTIONAL Specify project and version names)\n",
     'scan': '', 'size': '', 'dep': '', 'lic': '', 'rep': "",
     'detect_linux': " bash <(curl -s -L https://detect.synopsys.com/detect.sh)\n",
     'detect_linux_proxy': " (You may need to configure a proxy to download and run the Detect script as follows)\n" + \
                           " export DETECT_CURL_OPTS='--proxy http://USER:PASSWORD@PROXYHOST:PROXYPORT'\n" + \
                           " bash <(curl -s -L ${DETECT_CURL_OPTS} https://detect.synopsys.com/detect.sh)\n" + \
                           "--blackduck.proxy.host=PROXYHOST\n" + \
                           "--blackduck.proxy.port=PROXYPORT\n" + \
                           "--blackduck.proxy.username=USERNAME\n" + \
                           "--blackduck.proxy.password=PASSWORD\n",
     'detect_win': " powershell \"[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.synopsys.com/detect.ps1?$(Get-Random) | iex; detect\"\n",
     'detect_win_proxy': " (You may need to configure a proxy to download and run the Detect script as follows)\n" + \
                         "    ${Env:blackduck.proxy.host} = PROXYHOST\n" + \
                         "    ${Env:blackduck.proxy.port} = PROXYPORT\n" + \
                         "    ${Env:blackduck.proxy.password} = PROXYUSER\n" + \
                         "    ${Env:blackduck.proxy.username} = PROXYPASSWORD\n" + \
                         "    powershell \"[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.synopsys.com/detect.ps1?$(Get-Random) | iex; detect\"\n",
     'detect': ""}

rep = ''