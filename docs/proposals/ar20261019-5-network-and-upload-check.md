# AR-20261019-5: the api.notion.com setting and the Rohit upload check (Main 1, 19 Oct)

Prepared. Nothing is changed, uploaded or sent yet. Binary filing stays **blocked** until all steps below pass.

## Why a setting is needed

- The inbox routine runs in cloud environment env_01Pb9xdJdFEZj6Xuxuq5Kxid. This Main session runs there too.
- From here on 19 Oct at 12:58 UTC, a CONNECT to api.notion.com returned **403** from the environment's network policy.
- The file-upload flow (notion-create-file-upload, then one multipart POST to its upload_url) needs that host.
- Native source_url upload needs a public URL, and a Gmail attachment has none, as Main 2 checked first.
- Nothing broader is needed. No credentials are read.

## Step for Akshay (one setting)

1. Open the Main session, or any session in the same environment, on claude.ai/code.
2. Click the cloud environment menu in the session's title bar, then **Edit**.
3. Go to **Network access**. Under the **Limited** level, find **Allowed domains** and add `api.notion.com`. Leave **Allow package managers** ticked.
   - If the app shows **Custom** instead, add the same domain there and keep "include the default list of package managers" ticked.
4. Save. Don't change the access level, other domains or anything else.

The official steps are at https://code.claude.com/docs/en/cloud-environments#network-access.

## Check Main 1 runs after the setting (no test mail, no Prashant re-upload)

**Already staged, read-only, 19 Oct at 12:58 UTC:**
- **Source:** Gmail message 1a056589dddf7302 (ad@thepodium.in, 31 Aug 2026), RAW, saved to a file.
- **Part:** MIME part 2 is 16768.jpg (image/jpeg), **115,795 bytes, sha256 800a0253a8496d4b**. This matches Main 2's evidence.
- **Keys:** message key `mid:ddd162d5684f27bc`, file key `mid:ddd162d5684f27bc#2`.
- **Target:** Episode 3ed19a301a7f81c09fcbeb5d8be8e6a0 ("Rohit Manglik @ InfoBay.AI - Founder Thesis"), re-fetched. It has no "## Guest assets" section and no file block, so the file is genuinely missing there.

**After the setting:**
1. `curl https://api.notion.com/` from this session no longer gets a CONNECT 403. Any HTTP status from Notion itself counts as reachable.
2. Re-fetch the Episode. If a 16768.jpg block has appeared meanwhile, stop: it's already filed.
3. Make sure the Engagement's "## Assets to file" line exists, once.
4. notion-create-file-upload with filename 16768.jpg, then one multipart POST of the staged file to the upload_url, with every returned header.
5. Write under "## Guest assets" on the Episode (create the heading), newest first, the line below and directly under it the file block:
   - `2026-10-19 | Rohit Manglik (InfoBay.AI) | headshot | 16768.jpg | image/jpeg | 115795 bytes | sha256 800a0253a8496d4b | mid:ddd162d5684f27bc#2 | <cal: key if the Episode has one, else none>`
6. Readback:
   - Re-fetch the Episode with file URLs.
   - Download the block with curl into the scratch folder.
   - Confirm **115,795 bytes and sha256 800a0253a8496d4b**, and that the block sits directly under the keyed line.
   - Only then mark the pending line "filed 2026-10-19".
7. Report on the AR-5 task.

**Outcomes:**
- **All pass:** binary filing proven end to end in the routine's own environment.
- **POST still 403 or refused:** reason "upload blocked: <status>". Nothing filed, nothing claimed.
- **Readback mismatch:** the line stays pending ("page write not confirmed"). Investigate before integrating.

**Then, integration.** Only after cleanup accepts Main 2's section 6 fixes:
- Create the Controls page and put its 32-character id into the inbox passage.
- Compose the inbox against everything integrated, within the agreed headroom: AR-5 ships with at most one of AR-2 and AR-9 unless the reviewed trim lands first.
- Read back.

Automatic capture stays **unobserved** until a real incoming eligible file is filed by the inbox run.
