# Run sample

## Install

Make sure you have the correct version of Pydantic installed. You can install it using pip:

```sh
pip install pydantic==2.5.3
```

## Run examples

```powershell
python .\pydantic_demo.py
```

You should see output similar to:

```text
Running pydantic version:  2.5.3
id=1 name='Dr. Smith' office_hours=[OfficeHour(day='Monday', from_=9, to_=12), OfficeHour(day='Wednesday', from_=14, to_=17)]
{'id': 1, 'name': 'Dr. Smith', 'office_hours': [{'day': 'Monday', 'from_': 9, 'to_': 12}, {'day': 'Wednesday', 'from_': 14, 'to_': 17}]}
```
