# Back End Stuff

## Django prerequisities

* we'll use django as an api to front-end react framework
* the plan is when react calls api like

```bash
curl -X GET http://django_api_url/api/metric/covid_cases/india/<from_timestamp>to<to_timestamp>/

# this should return a json
{
    "country": "india",
    "metric": "covid_cases",
    "from_timestamp": "",
    "to_timestamp": "",
    "cases": ""
}
```

* the api should be able to handle timestamps, dates (years and months).
* the stream will be warehoused every seven days.
* so the timestamps from previous dates than seven days will return dates and total number of cases during the particular date.

## activating and install virtualenvironment

```bash
python3 -m venv pcovid_v1
source pcovid_v1/bin/activate
```

## django version

```python
>>> import django
>>> print(django.get_version())
3.1.3
>>>
```
