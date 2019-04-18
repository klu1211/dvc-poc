git pull origin master
branch_name=training_run/$(date +'%Y-%m-%d_%H-%M-%S')
git checkout -b $branch_name
aws s3 sync s3://dvc-root-data-bucket ./data
dvc repro
git add .
git commit -m "finished training run"
git push origin $branch_name
git checkout master
