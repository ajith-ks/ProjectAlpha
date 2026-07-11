# Dukascopy Protocol Research

**Document Version:** 1.0  
**Status:** Completed  
**Research Sprint:** RS-001

---

# Objective

Understand how Dukascopy historical market data is downloaded and stored so that Project Alpha can implement its own Python downloader without depending on third-party libraries.

This document contains architecture and protocol research only.

No source code from external projects will be copied into Project Alpha.

---

# Research Sources

## Official Documentation

- Dukascopy Historical Prices API
- Dukascopy Instruments API

## Open Source Reference

Repository:
https://github.com/theorycraft-trading/dukascopy

Purpose:
Understand the download protocol and binary format.

---

# Research Questions

| Question | Status |
|-----------|--------|
| Which endpoint is used? | ✅ |
| REST API or Data Feed? | ✅ |
| API Key Required? | ✅ |
| Compression Method | ✅ |
| Binary Format | ✅ |
| Instrument Mapping | ✅ |
| Price Conversion | ✅ |
| Timestamp Format | ✅ |
| Historical File Naming | ✅ |

---

# Findings

## Finding 1 — REST API

The documented REST API (`freeserv.dukascopy.com`) returned:

- HTTP 204
- Empty body

It is therefore **not suitable** for Project Alpha.

Decision:

**Rejected**

---

## Finding 2 — Historical Data Feed

The open-source implementation uses:

https://datafeed.dukascopy.com/datafeed

This is the historical data feed used for downloading market history.

Decision:

**Accepted**

---

## Finding 3 — Download Protocol

Historical data is downloaded as compressed binary files.

The downloader performs:

1. HTTP download
2. LZMA decompression
3. Binary parsing
4. Candle creation

No JSON is involved.

---

## Finding 4 — Compression

Downloaded files are compressed using

LZMA

Python equivalent:

```python
lzma
```

---

## Finding 5 — File Types

Minute

```
BID_candles_min_1.bi5
ASK_candles_min_1.bi5
```

Hour

```
BID_candles_hour_1.bi5
```

Day

```
BID_candles_day_1.bi5
```

---

## Finding 6 — URL Format

Minute candles

```
https://datafeed.dukascopy.com/datafeed/
<HistoricalFilename>/
<Year>/
<Month-1>/
<Day>/
BID_candles_min_1.bi5
```

Example

```
https://datafeed.dukascopy.com/datafeed/XAUUSD/2024/00/15/BID_candles_min_1.bi5
```

Important

- Month is zero-based.
- Day is one-based.

---

## Finding 7 — Instrument Mapping

Instrument names are converted into historical filenames.

Example

| Instrument | Historical Filename |
|------------|---------------------|
| EUR/USD | EURUSD |
| GBP/USD | GBPUSD |
| XAU/USD | XAUUSD |
| BTC/USD | BTCUSD |

Project Alpha will store this metadata locally.

---

## Finding 8 — Binary Record Layout

Each candle occupies **24 bytes**.

| Field | Type | Size |
|--------|------|------|
| Time Delta | int32 | 4 |
| Open | int32 | 4 |
| Close | int32 | 4 |
| Low | int32 | 4 |
| High | int32 | 4 |
| Volume | float32 | 4 |

Total

24 bytes

---

## Finding 9 — Time Encoding

Minute files

Time Delta

Seconds from midnight UTC.

Hour files

Seconds from first day of month.

Day files

Seconds from first day of year.

---

## Finding 10 — Price Encoding

Prices are stored as integers.

Conversion

```
Price = IntegerPrice / PointValue
```

Example

```
2056432 / 1000
```

↓

```
2056.432
```

---

## Finding 11 — Point Value

Formula

```
Point Value = 10 / Pip Value
```

Examples

| Instrument | Pip Value | Point Value |
|------------|----------:|------------:|
| EUR/USD | 0.0001 | 100000 |
| USD/JPY | 0.01 | 1000 |
| XAU/USD | 0.01 | 1000 |

---

## Finding 12 — Historical Start

Each instrument has an earliest available historical timestamp.

This will be stored in the metadata model.

---

# Accepted Architecture

```
HTTP Downloader
        │
        ▼
Download BI5 File
        │
        ▼
LZMA Decompressor
        │
        ▼
Binary Parser
        │
        ▼
OHLCV Objects
        │
        ▼
CSV Writer
        │
        ▼
Parquet Converter
        │
        ▼
Backtesting Engine
```

---

# Decisions

| ID | Decision |
|----|----------|
| DEC-001 | Do not use Dukascopy REST API |
| DEC-002 | Use Dukascopy Historical Data Feed |
| DEC-003 | Store raw downloads locally |
| DEC-004 | Store processed data as Parquet |
| DEC-005 | Maintain instrument metadata locally |

---

# Future Improvements

- Automatic metadata generation
- Local download cache
- Parallel downloads
- Resume interrupted downloads
- Incremental updates
- Multi-instrument downloads

---

# Conclusion

The research phase successfully identified the protocol used by Dukascopy historical data.

Project Alpha will implement its own downloader in Python using:

- HTTP downloads
- LZMA decompression
- Binary parsing
- Local metadata

No dependency on third-party Dukascopy libraries will exist in the final implementation.

Research Sprint RS-001 is complete.