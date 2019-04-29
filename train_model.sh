git pull origin master
branch_name=training_run/$(date +'%Y-%m-%d_%H-%M-%S')
git checkout -b $branch_name

# Pull down new data/models
dvc pull
aws s3 sync s3://dvc-root-data-bucket ./data

# Rerun training if there are any changes to our code or data
dvc repro

# Add changes and push them!
git add .
git commit -m "finished training run"
git push origin $branch_name

# Finally push these changes to DVC so that when we checkout this branch again we can pull the correct data down
dvc push


git checkout master
