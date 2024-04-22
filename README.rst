Google Cloud Python Client
==========================

Python idiomatic clients for `Google Cloud Platform`_ services.

.. _Google Cloud Platform: https://cloud.google.com/


Stability levels
*******************

The `development status classifier`_ on PyPI indicates the current stability
of a package.

.. _development status classifier: https://pypi.org/classifiers/

General Availability
--------------------

**GA** (general availability) indicates that the client library for a
particular service is stable, and that the code surface will not change in
backwards-incompatible ways unless absolutely necessary (e.g., due to
critical security issues) or with an extensive deprecation period.
Issues and requests against GA libraries are addressed with the highest
priority.

GA libraries have a development status classifier of ``Development Status :: 5 - Production/Stable``.

.. note::

    Sub-components of GA libraries explicitly marked as beta in the
    import path (e.g., ``google.cloud.language_v1beta2``) should be considered
    beta.

Beta Support
------------

**Beta** indicates that the client library for a particular service is
mostly stable and is being prepared for release. Issues and requests
against beta libraries are addressed with a higher priority.

Beta libraries have a development status classifier of ``Development Status :: 4 - Beta``.

Alpha Support
-------------

**Alpha** indicates that the client library for a particular service is
still a work-in-progress and is more likely to receive backwards-incompatible
updates. See `versioning`_ for more details.


Alpha libraries have a development status classifier of ``Development Status :: 3 - Alpha``.

If you need support for other Google APIs, check out the
`Google APIs Python Client library`_.

.. _Google APIs Python Client library: https://github.com/google/google-api-python-client


Libraries
*********

.. This table is generated, see synth.py for details.

.. list-table::
   :header-rows: 1

   * - Client
     - Release Level
     - Version
   * - `AI Platform <https://github.com/googleapis/python-aiplatform>`_
     - |stable|
     - |PyPI-google-cloud-aiplatform|
   * - `App Engine Admin <https://github.com/googleapis/python-appengine-admin>`_
     - |stable|
     - |PyPI-google-cloud-appengine-admin|
   * - `Asset Inventory <https://github.com/googleapis/python-asset>`_
     - |stable|
     - |PyPI-google-cloud-asset|
   * - `AutoML <https://github.com/googleapis/python-automl>`_
     - |stable|
     - |PyPI-google-cloud-automl|
   * - `BigQuery <https://github.com/googleapis/python-bigquery>`_
     - |stable|
     - |PyPI-google-cloud-bigquery|
   * - `BigQuery Storage <https://github.com/googleapis/python-bigquery-storage>`_
     - |stable|
     - |PyPI-google-cloud-bigquery-storage|
   * - `Bigtable <https://github.com/googleapis/python-bigtable>`_
     - |stable|
     - |PyPI-google-cloud-bigtable|
   * - `Binary Authorization <https://github.com/googleapis/python-binary-authorization>`_
     - |stable|
     - |PyPI-google-cloud-binary-authorization|
   * - `Build <https://github.com/googleapis/python-cloudbuild>`_
     - |stable|
     - |PyPI-google-cloud-build|
   * - `Common <https://github.com/googleapis/python-cloud-common>`_
     - |stable|
     - |PyPI-google-cloud-common|
   * - `Compute Engine <https://github.com/googleapis/python-compute>`_
     - |stable|
     - |PyPI-google-cloud-compute|
   * - `Container Analysis <https://github.com/googleapis/python-containeranalysis>`_
     - |stable|
     - |PyPI-google-cloud-containeranalysis|
   * - `Datastore <https://github.com/googleapis/python-datastore>`_
     - |stable|
     - |PyPI-google-cloud-datastore|
   * - `Filestore <https://github.com/googleapis/python-filestore>`_
     - |stable|
     - |PyPI-google-cloud-filestore|
   * - `Firestore <https://github.com/googleapis/python-firestore>`_
     - |stable|
     - |PyPI-google-cloud-firestore|
   * - `GKE Hub <https://github.com/googleapis/python-gke-hub>`_
     - |stable|
     - |PyPI-google-cloud-gke-hub|
   * - `Grafeas <https://github.com/googleapis/python-grafeas>`_
     - |stable|
     - |PyPI-grafeas|
   * - `Identity and Access Management <https://github.com/googleapis/python-grpc-google-iam-v1>`_
     - |stable|
     - |PyPI-grpc-google-iam-v1|
   * - `Key Management Service <https://github.com/googleapis/python-kms>`_
     - |stable|
     - |PyPI-google-cloud-kms|
   * - `Logging <https://github.com/googleapis/python-logging>`_
     - |stable|
     - |PyPI-google-cloud-logging|
   * - `Monitoring Dashboards <https://github.com/googleapis/python-monitoring-dashboards>`_
     - |stable|
     - |PyPI-google-cloud-monitoring-dashboards|
   * - `NDB Client Library for Datastore <https://github.com/googleapis/python-ndb>`_
     - |stable|
     - |PyPI-google-cloud-ndb|
   * - `OS Login <https://github.com/googleapis/python-oslogin>`_
     - |stable|
     - |PyPI-google-cloud-os-login|
   * - `Pandas Data Types for SQL systems (BigQuery, Spanner) <https://github.com/googleapis/python-db-dtypes-pandas>`_
     - |stable|
     - |PyPI-db-dtypes|
   * - `Pub/Sub <https://github.com/googleapis/python-pubsub>`_
     - |stable|
     - |PyPI-google-cloud-pubsub|
   * - `Pub/Sub Lite <https://github.com/googleapis/python-pubsublite>`_
     - |stable|
     - |PyPI-google-cloud-pubsublite|
   * - `Service Management <https://github.com/googleapis/python-service-management>`_
     - |stable|
     - |PyPI-google-cloud-service-management|
   * - `Spanner <https://github.com/googleapis/python-spanner>`_
     - |stable|
     - |PyPI-google-cloud-spanner|
   * - `Spanner Django <https://github.com/googleapis/python-spanner-django>`_
     - |stable|
     - |PyPI-django-google-spanner|
   * - `Speech <https://github.com/googleapis/python-speech>`_
     - |stable|
     - |PyPI-google-cloud-speech|
   * - `Stackdriver Monitoring <https://github.com/googleapis/python-monitoring>`_
     - |stable|
     - |PyPI-google-cloud-monitoring|
   * - `Storage <https://github.com/googleapis/python-storage>`_
     - |stable|
     - |PyPI-google-cloud-storage|
   * - `Trace <https://github.com/googleapis/python-trace>`_
     - |stable|
     - |PyPI-google-cloud-trace|
   * - `Translation <https://github.com/googleapis/python-translate>`_
     - |stable|
     - |PyPI-google-cloud-translate|
   * - `Vision <https://github.com/googleapis/python-vision>`_
     - |stable|
     - |PyPI-google-cloud-vision|
   * - `A unified Python API in BigQuery <https://github.com/googleapis/python-bigquery-dataframes>`_
     - |preview|
     - |PyPI-bigframes|
   * - `Analytics Admin <https://github.com/googleapis/python-analytics-admin>`_
     - |preview|
     - |PyPI-google-analytics-admin|
   * - `Analytics Data <https://github.com/googleapis/python-analytics-data>`_
     - |preview|
     - |PyPI-google-analytics-data|
   * - `Audit Log <https://github.com/googleapis/python-audit-log>`_
     - |preview|
     - |PyPI-google-cloud-audit-log|
   * - `BigQuery connector for pandas <https://github.com/googleapis/python-bigquery-pandas>`_
     - |preview|
     - |PyPI-pandas-gbq|
   * - `DNS <https://github.com/googleapis/python-dns>`_
     - |preview|
     - |PyPI-google-cloud-dns|
   * - `Dataflow <https://github.com/googleapis/python-dataflow-client>`_
     - |preview|
     - |PyPI-google-cloud-dataflow-client|
   * - `Document AI Toolbox <https://github.com/googleapis/python-documentai-toolbox>`_
     - |preview|
     - |PyPI-google-cloud-documentai-toolbox|
   * - `Error Reporting <https://github.com/googleapis/python-error-reporting>`_
     - |preview|
     - |PyPI-google-cloud-error-reporting|
   * - `Run <https://github.com/googleapis/python-run>`_
     - |preview|
     - |PyPI-google-cloud-run|
   * - `Runtime Configurator <https://github.com/googleapis/python-runtimeconfig>`_
     - |preview|
     - |PyPI-google-cloud-runtimeconfig|
   * - `SQLAlchemy dialect for BigQuery <https://github.com/googleapis/python-bigquery-sqlalchemy>`_
     - |preview|
     - |PyPI-sqlalchemy-bigquery|

.. |PyPI-google-cloud-aiplatform| image:: https://img.shields.io/pypi/v/google-cloud-aiplatform.svg
   :target: https://pypi.org/project/google-cloud-aiplatform
.. |PyPI-google-cloud-appengine-admin| image:: https://img.shields.io/pypi/v/google-cloud-appengine-admin.svg
   :target: https://pypi.org/project/google-cloud-appengine-admin
.. |PyPI-google-cloud-asset| image:: https://img.shields.io/pypi/v/google-cloud-asset.svg
   :target: https://pypi.org/project/google-cloud-asset
.. |PyPI-google-cloud-automl| image:: https://img.shields.io/pypi/v/google-cloud-automl.svg
   :target: https://pypi.org/project/google-cloud-automl
.. |PyPI-google-cloud-bigquery| image:: https://img.shields.io/pypi/v/google-cloud-bigquery.svg
   :target: https://pypi.org/project/google-cloud-bigquery
.. |PyPI-google-cloud-bigquery-storage| image:: https://img.shields.io/pypi/v/google-cloud-bigquery-storage.svg
   :target: https://pypi.org/project/google-cloud-bigquery-storage
.. |PyPI-google-cloud-bigtable| image:: https://img.shields.io/pypi/v/google-cloud-bigtable.svg
   :target: https://pypi.org/project/google-cloud-bigtable
.. |PyPI-google-cloud-binary-authorization| image:: https://img.shields.io/pypi/v/google-cloud-binary-authorization.svg
   :target: https://pypi.org/project/google-cloud-binary-authorization
.. |PyPI-google-cloud-build| image:: https://img.shields.io/pypi/v/google-cloud-build.svg
   :target: https://pypi.org/project/google-cloud-build
.. |PyPI-google-cloud-common| image:: https://img.shields.io/pypi/v/google-cloud-common.svg
   :target: https://pypi.org/project/google-cloud-common
.. |PyPI-google-cloud-compute| image:: https://img.shields.io/pypi/v/google-cloud-compute.svg
   :target: https://pypi.org/project/google-cloud-compute
.. |PyPI-google-cloud-containeranalysis| image:: https://img.shields.io/pypi/v/google-cloud-containeranalysis.svg
   :target: https://pypi.org/project/google-cloud-containeranalysis
.. |PyPI-google-cloud-datastore| image:: https://img.shields.io/pypi/v/google-cloud-datastore.svg
   :target: https://pypi.org/project/google-cloud-datastore
.. |PyPI-google-cloud-filestore| image:: https://img.shields.io/pypi/v/google-cloud-filestore.svg
   :target: https://pypi.org/project/google-cloud-filestore
.. |PyPI-google-cloud-firestore| image:: https://img.shields.io/pypi/v/google-cloud-firestore.svg
   :target: https://pypi.org/project/google-cloud-firestore
.. |PyPI-google-cloud-gke-hub| image:: https://img.shields.io/pypi/v/google-cloud-gke-hub.svg
   :target: https://pypi.org/project/google-cloud-gke-hub
.. |PyPI-grafeas| image:: https://img.shields.io/pypi/v/grafeas.svg
   :target: https://pypi.org/project/grafeas
.. |PyPI-grpc-google-iam-v1| image:: https://img.shields.io/pypi/v/grpc-google-iam-v1.svg
   :target: https://pypi.org/project/grpc-google-iam-v1
.. |PyPI-google-cloud-kms| image:: https://img.shields.io/pypi/v/google-cloud-kms.svg
   :target: https://pypi.org/project/google-cloud-kms
.. |PyPI-google-cloud-logging| image:: https://img.shields.io/pypi/v/google-cloud-logging.svg
   :target: https://pypi.org/project/google-cloud-logging
.. |PyPI-google-cloud-monitoring-dashboards| image:: https://img.shields.io/pypi/v/google-cloud-monitoring-dashboards.svg
   :target: https://pypi.org/project/google-cloud-monitoring-dashboards
.. |PyPI-google-cloud-ndb| image:: https://img.shields.io/pypi/v/google-cloud-ndb.svg
   :target: https://pypi.org/project/google-cloud-ndb
.. |PyPI-google-cloud-os-login| image:: https://img.shields.io/pypi/v/google-cloud-os-login.svg
   :target: https://pypi.org/project/google-cloud-os-login
.. |PyPI-db-dtypes| image:: https://img.shields.io/pypi/v/db-dtypes.svg
   :target: https://pypi.org/project/db-dtypes
.. |PyPI-google-cloud-pubsub| image:: https://img.shields.io/pypi/v/google-cloud-pubsub.svg
   :target: https://pypi.org/project/google-cloud-pubsub
.. |PyPI-google-cloud-pubsublite| image:: https://img.shields.io/pypi/v/google-cloud-pubsublite.svg
   :target: https://pypi.org/project/google-cloud-pubsublite
.. |PyPI-google-cloud-service-management| image:: https://img.shields.io/pypi/v/google-cloud-service-management.svg
   :target: https://pypi.org/project/google-cloud-service-management
.. |PyPI-google-cloud-spanner| image:: https://img.shields.io/pypi/v/google-cloud-spanner.svg
   :target: https://pypi.org/project/google-cloud-spanner
.. |PyPI-django-google-spanner| image:: https://img.shields.io/pypi/v/django-google-spanner.svg
   :target: https://pypi.org/project/django-google-spanner
.. |PyPI-google-cloud-speech| image:: https://img.shields.io/pypi/v/google-cloud-speech.svg
   :target: https://pypi.org/project/google-cloud-speech
.. |PyPI-google-cloud-monitoring| image:: https://img.shields.io/pypi/v/google-cloud-monitoring.svg
   :target: https://pypi.org/project/google-cloud-monitoring
.. |PyPI-google-cloud-storage| image:: https://img.shields.io/pypi/v/google-cloud-storage.svg
   :target: https://pypi.org/project/google-cloud-storage
.. |PyPI-google-cloud-trace| image:: https://img.shields.io/pypi/v/google-cloud-trace.svg
   :target: https://pypi.org/project/google-cloud-trace
.. |PyPI-google-cloud-translate| image:: https://img.shields.io/pypi/v/google-cloud-translate.svg
   :target: https://pypi.org/project/google-cloud-translate
.. |PyPI-google-cloud-vision| image:: https://img.shields.io/pypi/v/google-cloud-vision.svg
   :target: https://pypi.org/project/google-cloud-vision
.. |PyPI-bigframes| image:: https://img.shields.io/pypi/v/bigframes.svg
   :target: https://pypi.org/project/bigframes
.. |PyPI-google-analytics-admin| image:: https://img.shields.io/pypi/v/google-analytics-admin.svg
   :target: https://pypi.org/project/google-analytics-admin
.. |PyPI-google-analytics-data| image:: https://img.shields.io/pypi/v/google-analytics-data.svg
   :target: https://pypi.org/project/google-analytics-data
.. |PyPI-google-cloud-audit-log| image:: https://img.shields.io/pypi/v/google-cloud-audit-log.svg
   :target: https://pypi.org/project/google-cloud-audit-log
.. |PyPI-pandas-gbq| image:: https://img.shields.io/pypi/v/pandas-gbq.svg
   :target: https://pypi.org/project/pandas-gbq
.. |PyPI-google-cloud-dns| image:: https://img.shields.io/pypi/v/google-cloud-dns.svg
   :target: https://pypi.org/project/google-cloud-dns
.. |PyPI-google-cloud-dataflow-client| image:: https://img.shields.io/pypi/v/google-cloud-dataflow-client.svg
   :target: https://pypi.org/project/google-cloud-dataflow-client
.. |PyPI-google-cloud-documentai-toolbox| image:: https://img.shields.io/pypi/v/google-cloud-documentai-toolbox.svg
   :target: https://pypi.org/project/google-cloud-documentai-toolbox
.. |PyPI-google-cloud-error-reporting| image:: https://img.shields.io/pypi/v/google-cloud-error-reporting.svg
   :target: https://pypi.org/project/google-cloud-error-reporting
.. |PyPI-google-cloud-run| image:: https://img.shields.io/pypi/v/google-cloud-run.svg
   :target: https://pypi.org/project/google-cloud-run
.. |PyPI-google-cloud-runtimeconfig| image:: https://img.shields.io/pypi/v/google-cloud-runtimeconfig.svg
   :target: https://pypi.org/project/google-cloud-runtimeconfig
.. |PyPI-sqlalchemy-bigquery| image:: https://img.shields.io/pypi/v/sqlalchemy-bigquery.svg
   :target: https://pypi.org/project/sqlalchemy-bigquery

.. |ga| image:: https://img.shields.io/badge/support-GA-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability

.. |beta| image:: https://img.shields.io/badge/support-beta-orange.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#beta-support


.. |alpha| image:: https://img.shields.io/badge/support-alpha-orange.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#alpha-support


.. _PyPI: https://pypi.org/project/
.. _GA: ga
.. _beta: beta
.. _alpha: alpha

Introduction
=============

Google Cloud Platform (GCP) offers a wide array of services for building, deploying, and managing applications and services. The `Google Cloud Python Client`_ provides Python idiomatic clients for various GCP services, making it easier for developers to integrate GCP into their Python applications.

Stability Levels
================

The Google Cloud Python Client libraries are classified into different stability levels to indicate their current status and support level:

- **GA (General Availability):** Libraries marked as GA are considered stable, with no expected backwards-incompatible changes unless absolutely necessary. They receive the highest priority for issue resolution and support.

- **Beta Support:** Beta libraries are mostly stable but are still undergoing final testing and refinement before their official release. Issues and requests against beta libraries are addressed with a higher priority compared to alpha libraries.

- **Alpha Support:** Alpha libraries are still in active development and are more likely to undergo backwards-incompatible updates. They are considered works-in-progress and are suitable for experimentation but not recommended for production use.

Libraries
=========

The Google Cloud Python Client includes libraries for various GCP services. Here are some of the key libraries available:

- **AI Platform:** Provides Python clients for working with Google Cloud AI Platform.

- **App Engine Admin:** Allows managing Google App Engine applications programmatically.

- **Asset Inventory:** Offers Python clients for accessing the Asset Inventory API.

- **AutoML:** Provides Python idiomatic clients for Google Cloud AutoML.

- **BigQuery:** Includes Python clients for working with Google BigQuery.

- **BigQuery Storage:** Provides Python clients for accessing BigQuery Storage.

- **Bigtable:** Allows interacting with Google Cloud Bigtable using Python.

- **Binary Authorization:** Offers Python clients for the Binary Authorization API.

- **Build:** Provides Python clients for Google Cloud Build.

- **Common:** Contains common utilities and tools used across multiple Google Cloud services.

- **Compute Engine:** Offers Python clients for managing Google Compute Engine resources.

- **Container Analysis:** Provides Python clients for the Container Analysis API.

- **Datastore:** Includes Python clients for working with Google Cloud Datastore.

- **Filestore:** Allows interacting with Google Cloud Filestore using Python.

- **Firestore:** Provides Python clients for Google Cloud Firestore.

- **GKE Hub:** Offers Python clients for the GKE Hub API.

- **Grafeas:** Provides Python clients for interacting with the Grafeas API.

- **Identity and Access Management:** Allows managing IAM policies and permissions programmatically.

- **Key Management Service:** Provides Python clients for Google Cloud Key Management Service.

- **Logging:** Includes Python clients for accessing and managing Google Cloud Logging.

- **Monitoring Dashboards:** Provides Python clients for working with Google Cloud Monitoring Dashboards.

- **NDB Client Library for Datastore:** Offers an NDB client library for Google Cloud Datastore.

- **OS Login:** Allows managing OS login configurations programmatically.

- **Pandas Data Types for SQL systems:** Provides pandas data types for SQL systems like BigQuery and Spanner.

- **Pub/Sub:** Includes Python clients for Google Cloud Pub/Sub.

- **Pub/Sub Lite:** Provides Python clients for Google Cloud Pub/Sub Lite.

- **Service Management:** Allows managing Google Cloud services programmatically.

- **Spanner:** Includes Python clients for Google Cloud Spanner.

- **Spanner Django:** Offers Django integration with Google Cloud Spanner.

- **Speech:** Provides Python clients for Google Cloud Speech-to-Text and Text-to-Speech.

- **Stackdriver Monitoring:** Includes Python clients for Stackdriver Monitoring.

- **Storage:** Offers Python clients for working with Google Cloud Storage.

- **Trace:** Provides Python clients for Google Cloud Trace.

- **Translation:** Includes Python clients for Google Cloud Translation.

- **Vision:** Provides Python clients for Google Cloud Vision.

- **BigQuery Dataframes:** Offers a unified Python API for working with BigQuery.

- **Analytics Admin:** Provides Python clients for Google Analytics Admin API.

- **Analytics Data:** Offers Python clients for Google Analytics Data API.

- **Audit Log:** Provides Python clients for accessing Google Cloud Audit Logs.

- **BigQuery connector for pandas:** Allows using pandas with BigQuery.

- **DNS:** Offers Python clients for working with Google Cloud DNS.

- **Dataflow:** Provides Python clients for Google Cloud Dataflow.

- **Document AI Toolbox:** Includes Python clients for Google Cloud Document AI Toolbox.

- **Error Reporting:** Provides Python clients for Google Cloud Error Reporting.

- **Run:** Allows interacting with Google Cloud Run using Python.

- **Runtime Configurator:** Provides Python clients for Google Cloud Runtime Configurator.

- **SQLAlchemy dialect for BigQuery:** Allows using SQLAlchemy with BigQuery.

Each library has its own GitHub repository where you can find detailed documentation, examples, and installation instructions.

Conclusion
==========

The Google Cloud Python Client libraries offer a convenient way to interact with various Google Cloud services using Python. Whether you're working with data analytics, machine learning, or cloud infrastructure, these libraries provide a Pythonic interface to access GCP services efficiently. Choose the appropriate library based on your project's requirements and start building scalable and reliable applications on Google Cloud Platform.
