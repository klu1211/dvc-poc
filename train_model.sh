git pull origin master
branch_name=$(date +%x/%H/%M/%S)
git checkout -b training_run/$(branch_name)
aws s3 sync s3://dvc-root-data-bucket ./data --recursive
git add .
git push origin $(branch_name)
git checkout master
