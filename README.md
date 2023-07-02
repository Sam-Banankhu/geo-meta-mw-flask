# geo-meta-mw-flask
  Flask Repository

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project aims to provide an API for accessing the geographical metadata of areas in Malawi, including regions, districts, areas, and villages.

## Installation

To set up the API locally, follow these steps:

1. Clone the repository:

```shell
  $ git clone https://github.com/Sam-Banankhu/geo-meta-mw-flask.git
  $ cd geo-meta-mw-flask
```

2. Installing dependencies
```shell
  $ pip install -r requirements.txt
```

3. Set up the database:
```shell
  $ flask db create
```
This will create the necessary tables in the database.

## Usage
To run the API, execute the following command:
```shell
  $ flask run
```
The API will be accessible at `http://localhost:5000`.

You can use tools like cURL or Postman to make requests to the API endpoints and retrieve the geographical metadata for Malawi's regions, districts, areas, and villages.

## Contributing

Contributions to this project are welcome! To contribute, please follow these guidelines:

- Fork the repository and create a new branch for your feature or bug fix.
- Make your changes and ensure they are properly tested.
- Submit a pull request detailing your changes and the problem they solve.
- Please refer to the Contributing Guidelines for more information.

Please read the [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. For more details, see the LICENSE file.
```
  MIT License
```

For more information, see the [LICENSE](LICENSE) file.
