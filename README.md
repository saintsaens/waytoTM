# waytoTM
Merging all folders that were divided into separate artists when transcoding a lossless source from various artists.

- 10/27: Move all merged folders into single clean ready-to-upload folder.
- 10/25: Copy artwork from original folder to transcoded folders.
- 10/24: Merge folders.

## Initial state
General folder containing all albums in FLAC.
In each album there must be:
- all FLAC files
- optionally one or several .jpg or .png artwork files
- all transcoded folders with [320], [V0] or [V2] in their names

Example of file tree structure:
```
- FLACs
-- Various Artists - Album 1
--- Artist 1 - Album 1 [320] (containing transcoded mp3)
--- Artist 2 - Album 1 [320] (containing transcoded mp3)
--- Artist 1 - Album 1 [V0] (containing transcoded mp3)
--- Artist 2 - Album 1 [V0] (containing transcoded mp3)
--- Artist 1 - Album 1 [V2] (containing transcoded mp3)
--- Artist 2 - Album 1 [V2] (containing transcoded mp3)
--- Song1.flac
--- Song2.flac
--- Song3.flac
--- cover.jpg
--- cover.png
-- Various Artists - Album 2
--- Disc 1
---- Artist 1 - Album 2 [320] (containing transcoded mp3)
---- Artist 2 - Album 2 [320] (containing transcoded mp3)
---- Artist 1 - Album 2 [V0] (containing transcoded mp3)
---- Artist 2 - Album 2 [V0] (containing transcoded mp3)
---- Artist 1 - Album 2 [V2] (containing transcoded mp3)
---- Artist 2 - Album 2 [V2] (containing transcoded mp3)
---- Song2.flac
---- Song3.flac
---- Song4.flac
---- cover.jpg
---- cover.png
--- Disc 2
---- Artist 1 - Album 2 [320] (containing transcoded mp3)
---- Artist 2 - Album 2 [320] (containing transcoded mp3)
---- Artist 1 - Album 2 [V0] (containing transcoded mp3)
---- Artist 2 - Album 2 [V0] (containing transcoded mp3)
---- Artist 1 - Album 2 [V2] (containing transcoded mp3)
---- Artist 2 - Album 2 [V2] (containing transcoded mp3)
---- Song5.flac
---- Song6.flac
---- Song7.flac
- READY TO UPLOAD (empty)
```


## Final state
General folder containing all albums in FLAC (unchanged).
Ready-to-upload folder with:
- one merged folder for each [320], [V0] or [V2], with the artworks, even if album is divided into discs.
- optionally one or several .jpg or .png artwork files
```
- FLACs
[...] (same file tree structure as initial state)
- READY TO UPLOAD
-- Various Artists - Album 1 [320] (containing transcoded mp3 + artworks)
-- Various Artists - Album 1 [V0] (containing transcoded mp3 + artworks)
-- Various Artists - Album 1 [V2] (containing transcoded mp3 + artworks)
-- Various Artists - Album 2 [320]
--- Disc 1 (containing transcoded mp3 + artworks)
--- Disc 2 (containing transcoded mp3 + artworks)
-- Various Artists - Album 2 [V0]
--- Disc 1 (containing transcoded mp3 + artworks)
--- Disc 2 (containing transcoded mp3 + artworks)
-- Various Artists - Album 2 [V2]
--- Disc 1 (containing transcoded mp3 + artworks)
--- Disc 2 (containing transcoded mp3 + artworks)
```
