# Merchant Delivery 

## API Reference

### Merchants
__POST CREATE MERCHANT__
```json
{
    "name": "Mc Burguer"
}
```
__Response 201__
```json
{
    "id": "31fcclo9880-09eee2-de99001ccce40",
    "photo_url": "https://",
    "name": "Mc Burguer",
}
```
__Response 400__
```json
{
    "error": "Merchant already exists",
}
```