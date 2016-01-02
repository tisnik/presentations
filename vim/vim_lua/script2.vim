" Test script that uses the Lua interface to Vim

lua << EOF
local x = 6
local y = 7
print("The Answer to the Ultimate Question of Life, the Universe, and Everything: " .. x*y)
EOF

