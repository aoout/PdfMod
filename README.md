# PyPdf

## How to Install

```
pip install pypdf
```

## Basic Usage

```
pypdf toc read "D:\如何提问.pdf" notepad
```

```
pypdf toc write "D:\如何提问.pdf" --bias=8
```

```
pypdf delete "D:\如何提问.pdf" 0 25
```

```
pypdf join "D:\如何提问_上半.pdf" "D:\如何提问_下半.pdf"
```