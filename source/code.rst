.. _ngs-code:

Coding solutions
================


QC
--

.. _code-fastp:

Code: fastp
~~~~~~~~~~~

.. code:: bash

    # run fastp like this on the ancestor:
    $ fastp --detect_adapter_for_pe --overrepresentation_analysis --correction  --cut_right --html trimmed/anc.html --json trimmed/anc.json --thread 2 -i data/anc_R1.fastq.gz -I data/anc_R2.fastq.gz -o trimmed/anc_R1.fastq.gz -O trimmed/anc_R2.fastq.gz

    # run the evolved samples through fastp
    $ fastp --detect_adapter_for_pe --overrepresentation_analysis --correction --cut_right --html trimmed/evol1.html --json trimmed/evol1.json --thread 2 -i data/evol1_R1.fastq.gz -I data/evol1_R2.fastq.gz -o trimmed/evol1_R1.fastq.gz -O trimmed/evol1_R2.fastq.gz

    $ fastp --detect_adapter_for_pe --overrepresentation_analysis --correction --cut_right --html trimmed/evol2.html --json trimmed/evol2.json --thread 2 -i data/evol2_R1.fastq.gz -I data/evol2_R2.fastq.gz -o trimmed/evol2_R1.fastq.gz -O trimmed/evol2_R2.fastq.gz


.. _code-qc1:

Code: FastQC
~~~~~~~~~~~~

*Create directory:*

.. code:: bash

    $ mkdir trimmed-fastqc


*Run FastQC:*

.. code:: bash

    $ fastqc -o trimmed-fastqc trimmed/*.fastq.gz
  

*Run MultiQC*

.. code:: bash

    $ multiqc trimmed-fastqc


*Open |multiqc| report html webpage:*

.. code:: bash

   $ firefox multiqc_report.html



Assembly
--------

.. _code-assembly1:

Code: SPAdes assembly (trimmed data)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   spades.py -o assembly/spades-150/ -k 21,33,55,77 --careful -1 trimmed/ancestor-R1.trimmed.fastq.gz -2 trimmed/ancestor-R2.trimmed.fastq.gz


.. _code-assembly2:

Code: SPAdes assembly (original data)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   spades.py -o assembly/spades-original/ -k 21,33,55,77 --careful -1 data/ancestor-R1.fastq.gz -2 data/ancestor-R2.fastq.gz



Mapping
-------

.. _code-bowtie1:

Code: Bowtie2 indexing
~~~~~~~~~~~~~~~~~~~~~~

*Build the index:*

.. code:: bash

   bowtie2-build assembly/spades_final/scaffolds.fasta assembly/spades_final/scaffolds


.. _code-bowtie2:

Code: Bowtie2 mapping
~~~~~~~~~~~~~~~~~~~~~~

*Map to the genome. Use a max fragemnt length of 1000 bp:*

.. code:: bash

   bowtie2 -X 1000 -x assembly/spades_final/scaffolds -1 trimmed/evolved-6-R1.trimmed.fsatq.gz -2 trimmed/evolved-6-R2.trimmed.fastq.gz -S mappings/evolved-6.sam


.. _code-bwa1:

Code: BWA indexing
~~~~~~~~~~~~~~~~~~~~

*Index the genome assembly:*

.. code:: bash

   bwa index assembly/spades_final/scaffolds.fasta


.. _code-bwa2:

Code: BWA mapping
~~~~~~~~~~~~~~~~~~~

*Run bwa mem:*

.. code:: bash

   # trimmed data
   bwa mem assembly/spades_final/scaffolds.fasta trimmed/evolved-6-R1.trimmed.fastq.gz trimmed/evolved-6-R2.trimmed.fastq.gz > mappings/evolved-6.sam

   # raw data
   bwa mem assembly/spades_final/scaffolds.fasta data/evolved-6-R1.fastq.gz data/evolved-6-R2.fastq.gz > mappings/evolved-6.raw.sam