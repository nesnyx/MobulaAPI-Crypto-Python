
# Mobula API Cryptocurrency App use FastAPI

This is simple project build use FastAPI and data from Mobula API.<br>
![Logo](https://mobula.io/metaimage/Generic/others.png)
## Features

- Search Coins
- About
- Contact me
- SOON!



## Documentation
If you want to check out CMC API Documentation can go to through this link.
[CMC API Documentation](https://docs.mobula.io/introduction)



## Installation

You need do install some packages from venv and i provide <b>requirement.txt</b> for install packages what needed
and dont forget to make VENV in python or Virtual Enviroment
```bash
  python -m venv venv
  pip install -r requirement.txt
```
    
## API Reference

#### Get Coins

```http
  GET /coins
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your API key |
| `Content-Type` | `string` | **Required**. application/json |

#### Get Coins

```http
  GET /coins/search
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `coin`      | `string` | **Required**. From Input FORM |


#### About

```http
  GET /about
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `none`      | `none` | |




## Support

For support, email whycreation34@gmail.com.

