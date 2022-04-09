# Merchant Delivery 

## API Reference

### Merchants
__POST ACCESS TOKEN__
```json
{
    "email": "mcburguer@test.com",
	"password": "1234"
}
```
__Response 200__
```json
{
  	"access_token": "eyJ0eXAiOiJKV1asdnjkjkGGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0OTQzNzgyMSwianRpIjoiZWFhZDJjNzktMjRiNy00MDc2LWE2YzgtMzA5MzllMGJiMjJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImU0NTNlMjk4LWEzMDEtNDViOC1iMTU0LTRhNDhjOTJhZGI2OSIsIm5iZiI6MTY0OTQzNzgyMSwiZXhwIjoxNjQ5jEreA1q0XkChMeAGg"
}
```
__Response 401__
```json
{
    "error": "Password don't match!",
}
```

__POST CREATE MERCHANT__
```json
{
    "name": "Mc Burguer",
    "email": "mcburguer@test.com",
	"password": "1234"
}
```
__Response 201__
```json
{
    "id": "31fcclo9880-09eee2-de99001ccce40",
    "photo_url": "https://",
    "name": "Mc Burguer",
    "email": "mcburguer@test.com",
    "created_at": "2022-01-01"
}
```
__Response 400__
```json
{
    "error": "Merchant already exists",
}
```

### Address
__POST CREATE ADDRESS__
Protected endpoint
```json
{
	"street": "Rua ciclano",
	"state": "SP"
}
```
__Response 200__
```json
{
    "id": "76EEdc37-9787-437a-bjkad-4bads6d9633",
	"street": "Rua fulano",
	"state": "SP",
	"merchant_id": "e453e298-a301-45b8-b154-4a48c92adb69",
    "created_at": "Sat, 09 Apr 2022 16:37:08 GMT"
}
```
__Response 404__
```json
{
    "error": "Merchant not found."
}
```