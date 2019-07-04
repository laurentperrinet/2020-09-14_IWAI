default: github

SRC=2019-07-15_CNS

edit:
	atom $(SRC).py

page:
	python3 $(SRC).py
	# cat /tmp/talk.bib |pbcopy
	#atom ~/pool/blog/perrinet_curriculum-vitae_tex/LaurentPerrinet_Presentations.bib
	# academic ...

get_figures:
	mkdir -p figures
	# from the paper
	rsync -a ../WhereIsMyMNIST/paper/*.jpg figures

html: 
	python3 $(SRC).py index.html

show: html
#	open -a firefox $(SRC).html
	open /Applications/Safari.app/Contents/MacOS/Safari  index.html

github: html
	git add figures
	git commit --dry-run -am 'Test' | grep -q -v 'nothing to commit' && git commit -am' updating slides'
	git push
	open https://SpikeAI.github.io/$(SRC)

print: html
	#open -a /Applications/Chromium.app https://laurentperrinet.github.io/$(SRC)/?print-pdf&showNotes=true
	#open "https://laurentperrinet.github.io/$(SRC)/?print-pdf&showNotes=true"
	/Applications/Chromium.app/Contents/MacOS/Chromium --headless --disable-gpu --print-to-pdf=$(SRC).pdf "https://SpikeAI.github.io/$(SRC)/?print-pdf"
