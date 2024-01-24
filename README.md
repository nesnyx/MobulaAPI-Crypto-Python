
# Mobula API Cryptocurrency App use FastAPI

This is simple project build use FastAPI and data from Mobula API.
![Logo](https://mobula.io/metaimage/Generic/others.png)
## Features

- Search Coins
- About
- Contact me
- SOON!



## Documentation
If you want to check out CMC API Documentation can go to through this link.
[CMC API Documentation](https://coinmarketcap.com/api/documentation)



## Installation

You need do install some packages from venv and i provide <b>requirement.txt</b> for install packages what needed
and dont forget to make VENV in python or Virtual Enviroment
```bash
  python -m venv venv
  pip install -r requirement.txt
```
    
## API Reference

#### Get all Listing

```http
  GET /listing
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `X-CMC_PRO_API_KEY` | `string` | **Required**. Your API key |

#### Get Listing by Id

```http
  GET /listing/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


#### About

```http
  GET /about
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `none`      | `none` | |




## Support

For support, email whycreation34@gmail.com.

