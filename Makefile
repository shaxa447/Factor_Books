extract:
	pybabel extract --input-dirs=. -o locales/messages.pot

init:
	pybabel init -i locales/messages.pot -d locales -D messages -l en
	pybabel init -i locales/messages.pot -d locales -D messages -l uz
	pybabel init -i locales/messages.pot -d locales -D messages -l ko

compile_language:
	pybabel compile -d locales -D messages

update_languge:
	pybabel update -d locales -D messages -i locales/messages.pot