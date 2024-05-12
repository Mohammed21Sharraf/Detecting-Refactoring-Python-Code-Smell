def method_1(ExtractorError, manifest, playable, formats, asset, data, preplay, titles, title, description, duration, thumbnails, image, subtitles, sub, info, series, episode, programs):
        def call_playback_api(item, query=None):
            try:
                return self._call_api(f'playback/{item}/program/{video_id}', video_id, item, query=query)
            except ExtractorError as e:
                if isinstance(e.cause, HTTPError) and e.cause.status == 400:
                    return self._call_api(f'playback/{item}/{video_id}', video_id, item, query=query)
                raise

def method_2(ExtractorError, manifest, playable, formats, asset, data, preplay, titles, title, description, duration, thumbnails, image, subtitles, sub, info, series, episode, programs):
        formats = []
        for asset in playable['assets']:
            if not isinstance(asset, dict):
                continue
            if asset.get('encrypted'):
                continue
            format_url = url_or_none(asset.get('url'))
            if not format_url:
                continue
            asset_format = (asset.get('format') or '').lower()
            if asset_format == 'hls' or determine_ext(format_url) == 'm3u8':
                formats.extend(self._extract_nrk_formats(format_url, video_id))
            elif asset_format == 'mp3':
                formats.append({
                    'url': format_url,
                    'format_id': asset_format,
                    'vcodec': 'none',
                })

def method_3(ExtractorError, manifest, playable, formats, asset, data, preplay, titles, title, description, duration, thumbnails, image, subtitles, sub, info, series, episode, programs):
        thumbnails = []
        for image in try_get(
                preplay, lambda x: x['poster']['images'], list) or []:
            if not isinstance(image, dict):
                continue
            image_url = url_or_none(image.get('url'))
            if not image_url:
                continue
            thumbnails.append({
                'url': image_url,
                'width': int_or_none(image.get('pixelWidth')),
                'height': int_or_none(image.get('pixelHeight')),
            })

def method_4(ExtractorError, manifest, playable, formats, asset, data, preplay, titles, title, description, duration, thumbnails, image, subtitles, sub, info, series, episode, programs):
        subtitles = {}
        for sub in try_get(playable, lambda x: x['subtitles'], list) or []:
            if not isinstance(sub, dict):
                continue
            sub_url = url_or_none(sub.get('webVtt'))
            if not sub_url:
                continue
            sub_key = str_or_none(sub.get('language')) or 'nb'
            sub_type = str_or_none(sub.get('type'))
            if sub_type:
                sub_key += '-%s' % sub_type
            subtitles.setdefault(sub_key, []).append({
                'url': sub_url,
            })

def method_5(ExtractorError, manifest, playable, formats, asset, data, preplay, titles, title, description, duration, thumbnails, image, subtitles, sub, info, series, episode, programs):
        legal_age = try_get(
            data, lambda x: x['legalAge']['body']['rating']['code'], compat_str)
        # https://en.wikipedia.org/wiki/Norwegian_Media_Authority
        age_limit = None
        if legal_age:
            if legal_age == 'A':
                age_limit = 0
            elif legal_age.isdigit():
                age_limit = int_or_none(legal_age)

def method_6(ExtractorError, manifest, playable, formats, asset, data, preplay, titles, title, description, duration, thumbnails, image, subtitles, sub, info, series, episode, programs):
        info = {
            'id': video_id,
            'title': title,
            'alt_title': alt_title,
            'description': description,
            'duration': duration,
            'thumbnails': thumbnails,
            'age_limit': age_limit,
            'formats': formats,
            'subtitles': subtitles,
            'timestamp': parse_iso8601(try_get(manifest, lambda x: x['availability']['onDemand']['from'], str))
        }

def method_7(ExtractorError, manifest, playable, formats, asset, data, preplay, titles, title, description, duration, thumbnails, image, subtitles, sub, info, series, episode, programs):
        if is_series:
            series = season_id = season_number = episode = episode_number = None
            programs = self._call_api(
                'programs/%s' % video_id, video_id, 'programs', fatal=False)
            if programs and isinstance(programs, dict):
                series = str_or_none(programs.get('seriesTitle'))
                season_id = str_or_none(programs.get('seasonId'))
                season_number = int_or_none(programs.get('seasonNumber'))
                episode = str_or_none(programs.get('episodeTitle'))
                episode_number = int_or_none(programs.get('episodeNumber'))
            if not series:
                series = title
            if alt_title:
                title += ' - %s' % alt_title
            if not season_number:
                season_number = int_or_none(self._search_regex(
                    r'Sesong\s+(\d+)', description or '', 'season number',
                    default=None))
            if not episode:
                episode = alt_title if is_series else None
            if not episode_number:
                episode_number = int_or_none(self._search_regex(
                    r'^(\d+)\.', episode or '', 'episode number',
                    default=None))
            if not episode_number:
                episode_number = int_or_none(self._search_regex(
                    r'\((\d+)\s*:\s*\d+\)', description or '',
                    'episode number', default=None))
            info.update({
                'title': title,
                'series': series,
                'season_id': season_id,
                'season_number': season_number,
                'episode': episode,
                'episode_number': episode_number,
            })

