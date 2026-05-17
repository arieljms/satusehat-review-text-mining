from google_play_scraper import reviews, Sort
import pandas as pd

app_id = "com.telkom.tracencare"

result, _ = reviews(
    app_id,
    lang="id",
    country="id",
    sort=Sort.NEWEST,
    count=1500,
)

df = pd.DataFrame(result)
df = df[["reviewId", "content", "score", "at"]]
# df.to_csv("data/data_raw_satusehat.csv", index=False)