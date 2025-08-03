# suade

### Prerequisites
- lxml

### Installation
- pip install lxml

## Usage

**Validate a XML file:**
```python
python suade.py ./sample/FSA029-Sample-Valid.xml
```

**Validate all sample files:**
```python
python suade.py --all
```


## (a) What causes it to fail schema validation? Why do you think the regulator has included a valid file in their examples?

The invalid file fails schema validation because of unexpected element(s), in this case "IncorporatedEntities", "PartnershipsSoleTraders" and "LLPs" are all present within the "Capital" parent element, however "Capital" contains a choice element, and is expects only one element. A valid file has been provided to test against, to confirm the correct functionality of the system when correct input is given.

## (b) How would you fix the file to pass the schema validation?

To fix the file to pass the schema validation, I would omit elements to ensure that only one element within the Capital element is present. Firstly, it must be determined whether the business is a incorporated entity, LLP, sole trader or partnership, as they are mutually exclusive.


## (c) Why do you think the regulator has included an invalid file in their examples?

Invalid data demonstrates the unexpected edge cases that may arise from erroneous data input that need to be rectified by developers. The inclusion of invalid files encourages robust testing for validation logic by identifying errors and handling them gracefully; Overall, ensuring that the software functions correctly and requirements/regulatory compliance are met. 
