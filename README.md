# Sort Algorithms in Python [![BSD License][license-image]][license-url] [![Build Status][build-status]][build-repo]

This project contains several implementations of common sort algorithms in Python.

| Algorithm Name        | Best           | Average  | Worst | Memory | Stable | Method
| ------------- |:-------------:| -----:| -----:| -----:| -----:| -----:|
| BubbleSort | n |  n^2 | n^2 | 1 | Yes | Exchanging |
| CountingSort | - |  n+r | n+r | n+r | Yes | N/A |
| CycleSort | - |  n^2 | n^2 | 1 | No | Insertion |
| HeapSort | n log n |  n log n | n log n | 1 | No | Selection |
| InsertionSort | n |  n^2 | n^2 | 1 | Yes | Insertion |
| MergeSort | n log n |  n log n | n log n | n worst case | Yes | Merging |
| QuickSort | n log n | n log n | n^2 | log n  | Typically | Partitioning  |
| RadixSort | - |  n * k/d | n * k/d | 2^d | No | N/A |
| SelectionSort | n^2 |  n^2 | n^2 | 1 | No | Selection |

License
--------

*BSD License* --> A short, permissive software license. Basically, you can do whatever you want as long as you include the original copyright and license notice in any copy of the software/source.  There are many variations of this license in use.

[license-image]: http://img.shields.io/badge/license-BSD-blue.svg?style=flat
[license-url]: LICENSE
[build-status]: https://travis-ci.org/rahulnadella/Sort_Algorithms.svg?branch=master
[build-repo]: https://travis-ci.org/rahulnadella/Sort_Algorithms
