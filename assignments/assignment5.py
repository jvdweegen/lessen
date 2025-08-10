data = """company,industry,lead source,rating,page views,lead score,phone,title,status,email,website,sessions,created date
Abbott Laboratories  Utilities  Web  Cold  109  2  979-555-9715  Manager  Working - Contacted  seneker_pierette@abbott.com  35  2022-08-29 00:00:00.000
Moderna  Utilities  Web  Warm  47  4  306-555-2277  Analyst  Working - Contacted  rozenberg_wilden@modernatx.com  16  2022-11-11 00:00:00.000
Unknown  Utilities  Web  Warm  6  2  626-555-5435  Manager  Working - Contacted  fraaseelnora@icloud.com  1  2022-02-17 00:00:00.000
AT&T  Utilities  Web  Cold  58  5  272-555-6764  Assistant manager  Open - Not Contacted  corly@att.com  46  2022-04-07 00:00:00.000
Apple  Utilities  Web  Cold  139  3  189-555-2907    Open - Not Contacted  zwagerman_cecil@apple.com  130  2022-01-13 00:00:00.000
Unknown  Utilities  Web  Cold  7  2  620-555-5818  Administrative Analyst  Working - Contacted  dubourgroxine@smarttel.com.eg  1  2021-12-28 00:00:00.000
Unknown  Utilities  Web  Cold  109  4  485-555-6417    Working - Contacted  hiris@gmail.com  5  2022-04-17 00:00:00.000
Jabil  Utilities  Web  Warm  125  4  493-555-8336  Program Administrator  Working - Contacted  sewards_vince@jabil.com  93  2022-01-09 00:00:00.000
Danaher  Utilities  Web  Cold  102  2  461-555-5183  Office Manager  Working - Contacted  scheppmannshurlock@danaher.com  2  2022-09-20 00:00:00.000
Goldman Sachs Group  Utilities  Web  Cold  14  1  883-555-7567  Director  Open - Not Contacted  mcdermondlorenzo@goldmansachs.com  11  2022-07-23 00:00:00.000
Genuine Parts  Utilities  Web  Cold  49  2  715-555-3789  Supervisor  Working - Contacted  dewaardaamir@genpt.com  45  2022-09-15 00:00:00.000
NRG Energy  Utilities  Web  Cold  80  4  900-555-7187  Executive Assistant  Working - Contacted  chashim@nrg.com  61  2022-12-03 00:00:00.000
"""

lines = data.strip().split("\n")

headers = lines[0].split(",")
score_index = headers.index("lead score")

highest_score = None
lowest_score = None
highest_company = ""
lowest_company = ""

for row in lines[1:]:
    parts = row.split("  ")
    company = parts[0]
    score = int(parts[score_index])
    
    if highest_score is None or score > highest_score:
        highest_score = score
        highest_company = company
    
    if lowest_score is None or score < lowest_score:
        lowest_score = score
        lowest_company = company

print(f"Highest Lead Score: {highest_company} ({highest_score})")
print(f"Lowest Lead Score: {lowest_company} ({lowest_score})")
