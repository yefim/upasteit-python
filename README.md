## Usage (paste and get)

### Setup
``` python
>>> from upasteit import UPaste
>>> geoffs_pastes = UPaste("geoff")
```
### Paste
``` python
>>> geoffs_pastes.paste("hello there")
{
  "content": "hello there", 
  "created_at": "2012-12-02T22:10:04-05:00", 
  "user_id": 1, 
  "id": 1
}
```
### Paste more
``` python
>>> geoffs_pastes.paste(["first", "second", "potato"])
[
  {
    "content": "first", 
    "created_at": "2012-12-02T22:11:09-05:00", 
    "user_id": 1, 
    "id": 2
  }, 
  {
    "content": "second", 
    "created_at": "2012-12-02T22:11:10-05:00", 
    "user_id": 1, 
    "id": 3
  }, 
  {
    "content": "potato", 
    "created_at": "2012-12-02T22:11:10-05:00", 
    "user_id": 1, 
    "id": 4
  }
]
```
### Get Pastes
``` python
>>> geoffs_pastes.get()
[
  {
    "content": "second", 
    "created_at": "2012-12-02T22:11:10-05:00", 
    "user_id": 1, 
    "id": 3
  }, 
  {
    "content": "potato", 
    "created_at": "2012-12-02T22:11:10-05:00", 
    "user_id": 1, 
    "id": 4
  }, 
  {
    "content": "first", 
    "created_at": "2012-12-02T22:11:09-05:00", 
    "user_id": 1, 
    "id": 2
  }, 
  {
    "content": "hello there", 
    "created_at": "2012-12-02T22:10:04-05:00", 
    "user_id": 1, 
    "id": 1
  }
]
```
