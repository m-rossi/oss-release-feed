import argparse
import json
import xml.etree.ElementTree as ET

import requests


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('user', help='')
    parser.add_argument('-o', '--output', default='oss-releases.opml', help='')
    args = parser.parse_args()

    req = requests.request(
        'GET', f'https://api.github.com/users/{args.user}/starred')
    repos = []
    while 'next' in req.links:
        repos += json.loads(req.content)
        req = requests.request('GET', req.links['next']['url'])
    repos += json.loads(req.content)

    subscriptions = {}
    for r in repos:
        if r['language'] not in subscriptions:
            subscriptions[r['language']] = {}
        subscriptions[r['language']][r['full_name']] = {
            'htmlUrl': f'{r["html_url"]}/releases',
            'title': r['full_name'],
            'xmlUrl': f'{r["html_url"]}/releases.atom',
            'type': 'rss',
            'text': r['full_name'],
        }

    opml = ET.Element('opml', attrib={'version': '1.0'})
    for lang in subscriptions:
        if lang is not None:
            lang_xml = ET.Element(
                'outline', attrib={'text': lang,
                                   'title': lang})
        for sub in subscriptions[lang]:
            sub_xml = ET.Element('outline', attrib=subscriptions[lang][sub])
            if lang is None:
                opml.append(sub_xml)
            else:
                lang_xml.append(sub_xml)
        if lang is not None:
            opml.append(lang_xml)
    xml = ET.ElementTree(opml)
    xml.write(args.output)


if __name__ == '__main__':
    main()

