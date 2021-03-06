# Cookiecutter Simple

A simple example using <a href='https://github.com/cookiecutter/cookiecutter'>cookiecutter</a> and <a href='https://github.com/cruft/cruft'>cruft</a> to see how things fit together.

After a bit of searching, <a href='https://github.com/cookiecutter/cookiecutter/issues/784'>this</a> thread suggests that cookiecutter and cruft work well together, this repo exlores those claims by:

+ Evaluating how well cruft manages template updates
+ Evaluating how well this fits into GitHub actions for CI/CD

## Learnings

Step 1: clone using cruft

```
cruft create https://github.com/llabuschagne/cookiecutter-simple
```

Step 2: git init

```
git init
git checkout -b main
git remote add origin {{}}
git pull origin main
git add .
git commit -m 'initial commit'
git push origin main
```


