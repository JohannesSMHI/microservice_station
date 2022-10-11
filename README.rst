
SHARK station - microservice
==============================

🧰 About - Usage
-----------------

Developed by Shd at SMHI.

- Python based service using FastAPI
- Handles the versioned station.txt list at the Swedish NODC
- `Microservice Template <https://github.com/shark-microservices/microservice_template>`_


💻 Installation - Getting started
----------------------------------

**In production:**
Make sure to add environment variable "SHARK_STATION_LIST" with the path to the
versioned controlled station list file.

--------------------------------------------------------------------------------

**Create a virtual environment for your project with venv:**

.. code-block:: bash

    python -m venv venv

Activate the virtual environment:

.. code-block:: bash

    source ./venv/bin/activate

Install requirements with pip:

.. code-block:: bash

    pip install -r requirements.txt

--------------------------------------------------------------------------------

**Alternative with conda:**

.. code-block:: bash

    conda env create --file environment.yaml

Activate environment:

.. code-block:: bash

    conda activate py38
