git pull origin master
branch_name=training_run/$(date +%x/%H/%M/%S)
git checkout -b $branch_name
aws s3 sync s3://dvc-root-data-bucket ./data
dvc repro
git add .
git push origin $branch_name
git checkout master
