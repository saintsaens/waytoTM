# waytoTM
Merging all folders that were divided into separate artists when transcoding a lossless source from various artists.

- 10/25: Copy artwork from original folder to transcoded folders.
- 10/24: Merge folders.

## Initial state
General folder containing all albums in FLAC.
In each album there must be:
- all FLAC files
- optionally one or several .jpg or .png artwork files
- all transcoded folders with [320], [V0] or [V2] in their names
```
- FLACs
-- Album 1
--- Artist 1 - Album 1 [320]
--- Artist 2 - Album 1 [320]
--- Artist 1 - Album 1 [V0]
--- Artist 2 - Album 1 [V0]
--- Artist 1 - Album 1 [V2]
--- Artist 2 - Album 1 [V2]
--- Song1.flac
--- Song2.flac
--- Song3.flac
--- cover.jpg
--- cover.png
-- Album 2
--- Artist 1 - Album 2 [320]
--- Artist 2 - Album 2 [320]
--- Artist 1 - Album 2 [V0]
--- Artist 2 - Album 2 [V0]
--- Artist 1 - Album 2 [V2]
--- Artist 2 - Album 2 [V2]
--- Song1.flac
--- Song2.flac
--- Song3.flac
--- cover.jpg
--- cover.png
```


## Final state
General folder containing all albums in FLAC.
In each album there will be:
- all FLAC files (unchanged)
- optionally one or several .jpg or .png artwork files (unchanged)
- one merged folder for each [320], [V0] or [V2], with the artworks.
```
- FLACs
-- Album 1
--- Merged [320]
--- Merged [V0]
--- Merged [V2]
--- Song1.flac
--- Song2.flac
--- Song3.flac
--- cover.jpg
--- cover.png
-- Album 2
--- Merged [320]
--- Merged [V0]
--- Merged [V2]
--- Song1.flac
--- Song2.flac
--- Song3.flac
--- cover.jpg
--- cover.png
```
