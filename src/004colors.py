#\033[style;text;backm
#\033[0;33;44m

## ANSI pattern

#style          text          background
#0 - none       33 - white   - 40
#1 - bold       31 - red     - 41
#4 - underline  32 - green   - 42
#7 negative     33 - yellow  - 43
#               34 - blue    - 44
#               35 - magenta - 45
#               36 - ciano   - 46
#               37 - gray    - 47

print('\033[1;33;40m Fala Comigo!\033[m')
print('\033[7mOpa!\033[m')

color = {
  'clean' : '\033[m',
  'green' : '\033[4;32m'
}

print(f'{color['green']}Oooi{color['clean']}')