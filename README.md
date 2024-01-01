build application
gcloud builds submit --tag gcr.io/alien-hour-409923/Movie Recommender Project  --project=alien-hour-409923

deploy application
gcloud run deploy --image gcr.io/alien-hour-409923/Movie Recommender Project --platform managed  --project=alien-hour-409923 --allow-unauthenticated