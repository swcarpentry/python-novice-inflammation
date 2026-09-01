# Settings
ARCHIVE = 'python-novice-inflammation-code'
PYFILES = $(wildcard *.py)

# Controls
.PHONY : all commands test zip

all : commands

## commands         : show all commands (the default)
commands :
	@grep -h -E '^##' Makefile | sed -e 's/## //g'

## test             : test archive
test : zip
	@zip -T ${ARCHIVE}

## zip              : create python-novice-inflammation-code.zip
zip : ${ARCHIVE}

${ARCHIVE} : ${PYFILES}
	@cd .. && zip -9 -FS ./code/$@ -r ./code -i "*.py"
