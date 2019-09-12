import base64
Golde = b'aW1wb3J0IG1hcnNoYWwKZXhlYyhtYXJzaGFsLmxvYWRzKGInXHhlM1x4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDZceDAwXHgwMFx4MDBAXHgwMFx4MDBceDAwc1x4ZGVceDAwXHgwMFx4MDBkXHgwMGRceDAxbFx4MDBaXHgwMWRceDAwZFx4MDJsXHgwMG1ceDAyWlx4MDJceDAxXHgwMGRceDAwZFx4MDNsXHgwM1RceDAwZFx4MDBkXHgwMWxceDA0Wlx4MDRkXHgwMGRceDAxbFx4MDVaXHgwNWRceDA0Wlx4MDZkXHgwNVpceDA3ZFx4MDZaXHgwOGRceDA3Wlx0ZFx4MDhaXG5kXHRaXHgwYmRcblpceDBjZVx4MDdlXHgwNmVceDA4ZVx0ZVxuZVx4MGJmXHgwNlpccmVceDA0XHhhMFx4MGVlXHJceGExXHgwMVpceDA3ZVx4MGZlXHgwN1x4ODNceDAxXHgwMVx4MDBkXHgwYmRceDBjXHg4NFx4MDBaXHgxMGVceDExZFxyXHg4M1x4MDFaXHgxMmVceDEyalx4MTNkXHgwZWRceDBmZFx4MTBkXHgxMVx4OGRceDAzXHgwMVx4MDBlXHgxMlx4YTBceDE0XHhhMVx4MDBcXFx4MDJaXHgxNVpceDE2ZVx4MTVqXHgxN2RceDAxa1x4MDJyXHhiNmVceDA1XHhhMFx4MThkXHgxMlx4YTFceDAxXHgwMVx4MDBlXHgwZmVceDEyalx4MTlceDgzXHgwMVx4MDFceDAwbiRlXHgwNVx4YTBceDE4ZFx4MTJceGExXHgwMVx4MDFceDAwZVx4MGZkXHgxM2VceDBjXHgxN1x4MDBkXHgxM1x4MTdceDAwXHg4M1x4MDFceDAxXHgwMGVceDEwZVx4MTVqXHgxN1x4ODNceDAxXHgwMVx4MDBkXHgwMVNceDAwKVx4MTRceGU5XHgwMFx4MDBceDAwXHgwME4pXHgwMVx4ZGFceDA3UmVxdWVzdClceDAxXHhkYVx4MDEqelxuXHgxYlsxOzM0OzQwbXpcblx4MWJbMTszMTs0MG16XG5ceDFiWzE7Mzc7NDBtelxuXHgxYlsxOzMwOzQwbXpcblx4MWJbMTszMjs0MG16XG5ceDFiWzE7MzU7NDBtYWNceDAzXHgwMFx4MDBceDFiWzE7MzQ7NDBtXG4gICAgLyQkJCQkJCQkIC8kJCQkJCQkJC8kJCQkJCQkJCQgLyQkJCQkJCQkIC8kJCAgIC8kJFxuICAgfF9fICAkJF9fL3wgJCRfX19fXy98ICQkX18gICQkfCAkJF9fX19fL3wgJCQgIC8gJCRcbiAgICAgIHwgJCQgICB8ICQkICAgICAgfCAkJCAgXFwgJCR8ICQkICAgICAgfCAgJCQvICQkL1xuICAgICAgfCAkJCAgIHwgJCQkJCQgICB8ICQkJCQkJCQvfCAkJCQkJCAgICBcXCAgJCQkJC9cbiAgICAgIHwgJCQgICB8ICQkX18vICAgfCAkJF9fICAkJHwgJCRfXy8gICAgID4kJCAgJCRcbiAgICAgIHwgJCQgICB8ICQkICAgICAgfCAkJCAgXFwgJCR8ICQkICAgICAgIC8kJC9cXCAgJCRcbiAgICAgIHwgJCQgICB8ICQkJCQkJCQkfCAkJCAgfCAkJHwgJCQkJCQkJCR8ICQkICBcXCAkJFxuICAgICAgfF9fLyAgIHxfX19fX19fXy98X18vICB8X18vfF9fX19fX19fL3xfXy8gIHxfXy9cblxuICAgICAgXHgxYlsxOzMwOzQwbVtceDFiWzE7Mzc7NDBtK1x4MWJbMTszMDs0MG1dICAgICAgXHgxYlsxOzM0OzQwbUZhY2VCb29rIFx4MWJbMTszMTs0MG06IFx4MWJbMTszNzs0MG1BYmR1bHJobWFuQWx3c2FieSAgICAgIFx4MWJbMTszMDs0MG1bXHgxYlsxOzM3OzQwbStceDFiWzE7MzA7NDBtXVxuICAgICAgXHgxYlsxOzMwOzQwbVtceDFiWzE7Mzc7NDBtK1x4MWJbMTszMDs0MG1dICAgICAgXHgxYlsxOzM0OzQwbVRlbGVHcmFtIFx4MWJbMTszMTs0MG06IFx4MWJbMTszNzs0MG1BYmR1bHJobWFuQWx3c2FieSAgICAgIFx4MWJbMTszMDs0MG1bXHgxYlsxOzM3OzQwbStceDFiWzE7MzA7NDBtXVxuXG4gICAgICAgLS0tLS0tLS0tLS0tPT09PT09XHgxYlsxOzM0OzQwbVtceDFiWzE7Mzc7NDBtVEVSRVhceDFiWzE7MzQ7NDBtXVx4MWJbMTszMDs0MG09PT09PT0tLS0tLS0tLS0tLS1cbiAgICAgICAgICAgICAgICAgICAgIFx4MWJbMTszMTs0MG09PT09PT09PT09PT09PT1cbmNceDAxXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDZceDAwXHgwMFx4MDBceDlmXHgwMVx4MDBceDAwQ1x4MDBceDAwXHgwMHNgXHgwNVx4MDBceDAwXHg5MFx4MDV5Rlx4OTBceDA1eVx4MDZ0XHgwMGpceDAxXHhhMFx4MDJ8XHgwMFx4YTFceDAxfVx4MDFkXHgwMWRceDAyZFx4MDNkXHgwNGRceDA1ZFx4MDZkXHgwN2RceDA4ZFx0ZFxuZFx4MGJkXHgwY2RccmRceDBlZFx4MGZkXHgxMGRceDExZFx4MTJkXHgxM2RceDE0ZFx4MTVkXHgxNmRceDE3ZFx4MThkXHgxOWRceDFhZFx4MWJkXHgxY2RceDFkZFx4MWVkXHgxZmQgZCFkImQjZCRkJWQmZFwnZChkKWQqZCtkLGQtZC5kL2QwZDFkMmQzZDRkNWQ2ZDdkOGQ5ZDpkO2Q8ZD1kPmQ/ZEBkQWRCZENkRGRFZEZkR2RIZElkSmRLZExkTWROZE9kUGRRZFJkU2RUZFVkVmRXZFhkWWRaZFtkXFxkXWReZF9kYGRhZGJkY2RkZGVkZmRnZGhkaWRqZGtkbGRtZG5kb2RwZHFkcmRzZHRkdWR2ZHdkeGR5ZHpke2R8ZH1kfmRceDdmZFx4ODBkXHg4MWRceDgyZFx4ODNkXHg4NGRceDg1ZFx4ODZkXHg4N2RceDg4ZFx4ODlkXHg4YWRceDhiZFx4OGNkXHg4ZGRceDhlZFx4OGZkXHg5MGRceDkxZFx4OTJkXHg5M2RceDk0ZFx4OTVkXHg5NmRceDk3ZFx4OThkXHg5OWRceDlhZFx4OWJkXHg5Y2RceDlkZFx4OWVkXHg5ZmRceGEwZFx4YTFkXHhhMmRceGEzZFx4YTRkXHhhNWRceGE2ZFx4YTdkXHhhOGRceGE5ZFx4YWFkXHhhYmRceGFjZFx4YWRkXHhhZWRceGFmZFx4YjBkXHhiMWRceGIyZFx4YjNkXHhiNGRceGI1ZFx4YjZkXHhiN2RceGI4ZFx4YjlkXHhiYWRceGJiZFx4YmNkXHhiZGRceGJlZFx4YmZkXHhjMGRceGMxZFx4YzJkXHhjM2RceGM0ZFx4YzVkXHhjNmRceGM3ZFx4YzhkXHhjOWRceGNhZFx4Y2JkXHhjY2RceGNkZFx4Y2VkXHhjZmRceGQwZFx4ZDFkXHhkMmRceGQzZFx4ZDRkXHhkNWRceGQ2ZFx4ZDdkXHhkOGRceGQ5ZFx4ZGFkXHhkYmRceGRjZFx4ZGRkXHhkZWRceGRmZFx4ZTBkXHhlMWRceGUyZFx4ZTNkXHhlNGRceGU1ZFx4ZTZkXHhlN2RceGU4ZFx4ZTlkXHhlYWRceGViZFx4ZWNkXHhlZGRceGVlZFx4ZWZkXHhmMGRceGYxZFx4ZjJkXHhmM2RceGY0ZFx4ZjVkXHhmNmRceGY3ZFx4ZjhkXHhmOWRceGZhZFx4ZmJkXHhmY2RceGZkZFx4ZmVkXHhmZlx4OTBceDAxZFx4MDBceDkwXHgwMWRceDAxXHg5MFx4MDFkXHgwMlx4OTBceDAxZFx4MDNceDkwXHgwMWRceDA0XHg5MFx4MDFkXHgwNVx4OTBceDAxZFx4MDZceDkwXHgwMWRceDA3XHg5MFx4MDFkXHgwOFx4OTBceDAxZFx0XHg5MFx4MDFkXG5ceDkwXHgwMWRceDBiXHg5MFx4MDFkXHgwY1x4OTBceDAxZFxyXHg5MFx4MDFkXHgwZVx4OTBceDAxZFx4MGZceDkwXHgwMWRceDEwXHg5MFx4MDFkXHgxMVx4OTBceDAxZFx4MTJceDkwXHgwMWRceDEzXHg5MFx4MDFkXHgxNFx4OTBceDAxZFx4MTVceDkwXHgwMWRceDE2XHg5MFx4MDFkXHgxN1x4OTBceDAxZFx4MThceDkwXHgwMWRceDE5XHg5MFx4MDFkXHgxYVx4OTBceDAxZFx4MWJceDkwXHgwMWRceDFjXHg5MFx4MDFkXHgxZFx4OTBceDAxZFx4MWVceDkwXHgwMWRceDFmXHg5MFx4MDFkIFx4OTBceDAxZCFceDkwXHgwMWQiXHg5MFx4MDFkI1x4OTBceDAxZCRceDkwXHgwMWQlXHg5MFx4MDFkJlx4OTBceDAxZFwnXHg5MFx4MDFkKFx4OTBceDAxZClceDkwXHgwMWQqXHg5MFx4MDFkK1x4OTBceDAxZCxceDkwXHgwMWQtXHg5MFx4MDFkLlx4OTBceDAxZC9ceDkwXHgwMWQwXHg5MFx4MDFkMVx4OTBceDAxZDJceDkwXHgwMWQzXHg5MFx4MDFkNFx4OTBceDAxZDVceDkwXHgwMWQ2XHg5MFx4MDFkN1x4OTBceDAxZDhceDkwXHgwMWQ5XHg5MFx4MDFkOlx4OTBceDAxZDtceDkwXHgwMWQ8XHg5MFx4MDFkPVx4OTBceDAxZD5ceDkwXHgwMWQ/XHg5MFx4MDFkQFx4OTBceDAxZEFceDkwXHgwMWRCXHg5MFx4MDFkQ1x4OTBceDAxZERceDkwXHgwMWRFXHg5MFx4MDFkRlx4OTBceDAxZEdceDkwXHgwMWRIXHg5MFx4MDFkSVx4OTBceDAxZEpceDkwXHgwMWRLXHg5MFx4MDFkTFx4OTBceDAxZE1ceDkwXHgwMWROXHg5MFx4MDFkT1x4OTBceDAxZFBceDkwXHgwMWRRXHg5MFx4MDFkUlx4OTBceDAxZFNceDkwXHgwMWRUXHg5MFx4MDFkVVx4OTBceDAxZFZceDkwXHgwMWRXXHg5MFx4MDFkWFx4OTBceDAxZFlceDkwXHgwMWRaXHg5MFx4MDFkW1x4OTBceDAxZFxcXHg5MFx4MDFkXVx4OTBceDAxZF5ceDkwXHgwMWRfXHg5MFx4MDFkYFx4OTBceDAxZGFceDkwXHgwMWRiXHg5MFx4MDFkY1x4OTBceDAxZGRceDkwXHgwMWRlXHg5MFx4MDFkZlx4OTBceDAxZGdceDkwXHgwMWRoXHg5MFx4MDFkaVx4OTBceDAxZGpceDkwXHgwMWRrXHg5MFx4MDFkbFx4OTBceDAxZG1ceDkwXHgwMWRuXHg5MFx4MDFkb1x4OTBceDAxZHBceDkwXHgwMWRxXHg5MFx4MDFkclx4OTBceDAxZHNceDkwXHgwMWR0XHg5MFx4MDFkdVx4OTBceDAxZHZceDkwXHgwMWR3XHg5MFx4MDFkeFx4OTBceDAxZHlceDkwXHgwMWR6XHg5MFx4MDFke1x4OTBceDAxZHxceDkwXHgwMWR9XHg5MFx4MDFkflx4OTBceDAxZFx4N2ZceDkwXHgwMWRceDgwXHg5MFx4MDFkXHg4MVx4OTBceDAxZFx4ODJceDkwXHgwMWRceDgzXHg5MFx4MDFkXHg4NFx4OTBceDAxZFx4ODVceDkwXHgwMWRceDg2XHg5MFx4MDFkXHg4N1x4OTBceDAxZFx4ODhceDkwXHgwMWRceDg5XHg5MFx4MDFkXHg4YVx4OTBceDAxZFx4OGJceDkwXHgwMWRceDhjXHg5MFx4MDFkXHg4ZFx4OTBceDAxZFx4OGVceDkwXHgwMWRceDhmXHg5MFx4MDFkXHg5MFx4OTBceDAxZFx4OTFceDkwXHgwMWRceDkyXHg5MFx4MDFkXHg5M1x4OTBceDAxZFx4OTRceDkwXHgwMWRceDk1XHg5MFx4MDFkXHg5Nlx4OTBceDAxZFx4OTdceDkwXHgwMWRceDk4XHg5MFx4MDFkXHg5OVx4OTBceDAxZFx4OWFceDkwXHgwMWRceDliXHg5MFx4MDFkXHg5Y1x4OTBceDAxZFx4OWRceDkwXHgwMWRceDllXHg5MFx4MDFkXHg5Zlx4OTBceDAxZ1x4OWZ9XHgwMnhwfFx4MDJEXHgwMF1ofVx4MDN8XHgwMFx4OTBceDAxZFx4YTBceDE3XHgwMHxceDAzXHgxN1x4MDB9XHgwNHkkdFx4MDBqXHgwMVx4YTBceDAyfFx4MDRceGExXHgwMX1ceDAxdFx4MDNceDkwXHgwMWRceGExfFx4MDRceDE3XHgwMFx4OTBceDAxZFx4YTJceDE3XHgwMFx4ODNceDAxXHgwMVx4MDBXXHgwMG4uXHgwNFx4MDB0XHgwMGpceDAxalx4MDRrXG5ceDkwXHgwNXJceDAyXHgwMVx4MDBceDAxXHgwMFx4MDFceDAwdFx4MDNceDkwXHgwMWRceGEzfFx4MDRceDE3XHgwMFx4OTBceDAxZFx4YTRceDE3XHgwMFx4ODNceDAxXHgwMVx4MDBZXHgwMG5ceDAyWFx4MDBceDkwXHgwNHFceDllV1x4MDBXXHgwMG44XHgwNFx4MDB0XHgwMGpceDAxalx4MDVrXG5ceDkwXHgwNXJEXHgwMVx4MDB9XHgwNVx4MDFceDAwelx4MTR0XHgwM3xceDAwXHg4M1x4MDFceDAxXHgwMHRceDAzfFx4MDVceDgzXHgwMVx4MDFceDAwV1x4MDBkXHgwMGRceDAwfVx4MDV+XHgwNVhceDAwWVx4MDBuXHgwMlhceDAwV1x4MDBuXHgxMlx4MDFceDAwXHgwMVx4MDBceDAxXHgwMHRceDA2XHg4M1x4MDBceDAxXHgwMFlceDAwblx4MDJYXHgwMGRceDAwU1x4MDAoXHhhNVx4MDFceDAwXHgwME56XHgwNmFkbWluL3pceDBlYWRtaW5pc3RyYXRvci96XHgwN2FkbWluMS96XHgwN2FkbWluMi96XHgwN2FkbWluMy96XHgwN2FkbWluNC96XHgwN2FkbWluNS96XHR1c3Vhcmlvcy96XHgwOHVzdWFyaW8velxubW9kZXJhdG9yL3pcdHdlYmFkbWluL3pcbmFkbWluYXJlYS96XHRiYi1hZG1pbi96XHgwYmFkbWluTG9naW4velx4MGJhZG1pbl9hcmVhL3pceDE1cGFuZWwtYWRtaW5pc3RyYWNpb24velxuaW5zdGFkbWluL3pceDBjbWVtYmVyYWRtaW4velx4MTNhZG1pbmlzdHJhdG9ybG9naW4velx4MDRhZG0velx4MTFhZG1pbi9hY2NvdW50LnBocHpceDBmYWRtaW4vaW5kZXgucGhwelx4MGZhZG1pbi9sb2dpbi5waHB6XHgwZmFkbWluL2FkbWluLnBocHpceDE0YWRtaW5fYXJlYS9hZG1pbi5waHB6XHgxNGFkbWluX2FyZWEvbG9naW4ucGhwelx4MTNzaXRlYWRtaW4vbG9naW4ucGhwelx4MTNzaXRlYWRtaW4vaW5kZXgucGhwelx4MTRzaXRlYWRtaW4vbG9naW4uaHRtbHpceDEyYWRtaW4vYWNjb3VudC5odG1selx4MTBhZG1pbi9pbmRleC5odG1selx4MTBhZG1pbi9sb2dpbi5odG1selx4MTBhZG1pbi9hZG1pbi5odG1selx4MTRhZG1pbl9hcmVhL2luZGV4LnBocHpceDEyYmItYWRtaW4vaW5kZXgucGhwelx4MTJiYi1hZG1pbi9sb2dpbi5waHB6XHgxMmJiLWFkbWluL2FkbWluLnBocHpceDBlYWRtaW4vaG9tZS5waHB6XHgxNWFkbWluX2FyZWEvbG9naW4uaHRtbHpceDE1YWRtaW5fYXJlYS9pbmRleC5odG1selx4MTZhZG1pbi9jb250cm9scGFuZWwucGhwelx0YWRtaW4ucGhwelx4MTFhZG1pbmNwL2luZGV4LmFzcHpceDExYWRtaW5jcC9sb2dpbi5hc3B6XHgxMmFkbWluY3AvaW5kZXguaHRtbHpceDBmYWRtaW5wYW5lbC5odG1selxyd2ViYWRtaW4uaHRtbHpceDEzd2ViYWRtaW4vaW5kZXguaHRtbHpceDEzd2ViYWRtaW4vYWRtaW4uaHRtbHpceDEzd2ViYWRtaW4vbG9naW4uaHRtbHpceDE2YWRtaW4vYWRtaW5fbG9naW4uaHRtbHpceDEwYWRtaW5fbG9naW4uaHRtbHpceDFmcGFuZWwtYWRtaW5pc3RyYWNpb24vbG9naW4uaHRtbHpceDBjYWRtaW4vY3AucGhwelx4MDZjcC5waHB6XHgxN2FkbWluaXN0cmF0b3IvaW5kZXgucGhwelx4MTdhZG1pbmlzdHJhdG9yL2xvZ2luLnBocHpceDEzbnN3L2FkbWluL2xvZ2luLnBocHpceDEyd2ViYWRtaW4vbG9naW4ucGhwelx4MTVhZG1pbi9hZG1pbl9sb2dpbi5waHB6XHgwZmFkbWluX2xvZ2luLnBocHpceDE5YWRtaW5pc3RyYXRvci9hY2NvdW50LnBocHpceDExYWRtaW5pc3RyYXRvci5waHB6XHgxNWFkbWluX2FyZWEvYWRtaW4uaHRtbHpceDFicGFnZXMvYWRtaW4vYWRtaW4tbG9naW4ucGhwelx4MTVhZG1pbi9hZG1pbi1sb2dpbi5waHB6XHgwZmFkbWluLWxvZ2luLnBocHpceDEzYmItYWRtaW4vaW5kZXguaHRtbHpceDEzYmItYWRtaW4vbG9naW4uaHRtbHpcbmFjY2Vzby5waHB6XHgxM2JiLWFkbWluL2FkbWluLmh0bWx6XHgwZmFkbWluL2hvbWUuaHRtbHpcdGxvZ2luLnBocHpceDE1bW9kZWxzZWFyY2gvbG9naW4ucGhwelxybW9kZXJhdG9yLnBocHpceDEzbW9kZXJhdG9yL2xvZ2luLnBocHpceDEzbW9kZXJhdG9yL2FkbWluLnBocHpceDBiYWNjb3VudC5waHB6XHgxY3BhZ2VzL2FkbWluL2FkbWluLWxvZ2luLmh0bWx6XHgxNmFkbWluL2FkbWluLWxvZ2luLmh0bWx6XHgxMGFkbWluLWxvZ2luLmh0bWx6XHgxMGNvbnRyb2xwYW5lbC5waHB6XHgxMGFkbWluY29udHJvbC5waHB6XHgxNWFkbWluL2FkbWluTG9naW4uaHRtbHpceDBmYWRtaW5Mb2dpbi5odG1selx0aG9tZS5odG1selx4MTdyY2pha2FyL2FkbWluL2xvZ2luLnBocHpceDE0YWRtaW5hcmVhL2luZGV4Lmh0bWx6XHgxNGFkbWluYXJlYS9hZG1pbi5odG1selx4MGN3ZWJhZG1pbi5waHB6XHgxMndlYmFkbWluL2luZGV4LnBocHpceDEyd2ViYWRtaW4vYWRtaW4ucGhwelx4MTdhZG1pbi9jb250cm9scGFuZWwuaHRtbHpcbmFkbWluLmh0bWx6XHJhZG1pbi9jcC5odG1selx4MDdjcC5odG1selx4MGVhZG1pbnBhbmVsLnBocHpceDBlbW9kZXJhdG9yLmh0bWx6XHgxOGFkbWluaXN0cmF0b3IvaW5kZXguaHRtbHpceDE4YWRtaW5pc3RyYXRvci9sb2dpbi5odG1selx0dXNlci5odG1selx4MWFhZG1pbmlzdHJhdG9yL2FjY291bnQuaHRtbHpceDEyYWRtaW5pc3RyYXRvci5odG1selxubG9naW4uaHRtbHpceDE2bW9kZWxzZWFyY2gvbG9naW4uaHRtbHpceDE0bW9kZXJhdG9yL2xvZ2luLmh0bWx6XHgxNGFkbWluYXJlYS9sb2dpbi5odG1selx4MWZwYW5lbC1hZG1pbmlzdHJhY2lvbi9pbmRleC5odG1selx4MWZwYW5lbC1hZG1pbmlzdHJhY2lvbi9hZG1pbi5odG1selx4MTZtb2RlbHNlYXJjaC9pbmRleC5odG1selx4MTZtb2RlbHNlYXJjaC9hZG1pbi5odG1selx4MTdhZG1pbmNvbnRyb2wvbG9naW4uaHRtbHpceDBlYWRtL2luZGV4Lmh0bWx6XHgwOGFkbS5odG1selx4MTRtb2RlcmF0b3IvYWRtaW4uaHRtbHpceDA4dXNlci5waHB6XHgwY2FjY291bnQuaHRtbHpceDExY29udHJvbHBhbmVsLmh0bWx6XHgxMWFkbWluY29udHJvbC5odG1selx4MWVwYW5lbC1hZG1pbmlzdHJhY2lvbi9sb2dpbi5waHB6XHgwY3dwLWxvZ2luLnBocHpceDBlYWRtaW5Mb2dpbi5waHB6XHgxNGFkbWluL2FkbWluTG9naW4ucGhwelx4MDhob21lLnBocHpceDEzYWRtaW5hcmVhL2luZGV4LnBocHpceDEzYWRtaW5hcmVhL2FkbWluLnBocHpceDEzYWRtaW5hcmVhL2xvZ2luLnBocHpceDFlcGFuZWwtYWRtaW5pc3RyYWNpb24vaW5kZXgucGhwelx4MWVwYW5lbC1hZG1pbmlzdHJhY2lvbi9hZG1pbi5waHB6XHgxNW1vZGVsc2VhcmNoL2luZGV4LnBocHpceDE1bW9kZWxzZWFyY2gvYWRtaW4ucGhwelx4MTZhZG1pbmNvbnRyb2wvbG9naW4ucGhwelx4MTRhZG0vYWRtbG9naW51c2VyLnBocHpceDEwYWRtbG9naW51c2VyLnBocHpcbmFkbWluMi5waHB6XHgxMGFkbWluMi9sb2dpbi5waHB6XHgxMGFkbWluMi9pbmRleC5waHB6XHgxMnVzdWFyaW9zL2xvZ2luLnBocHpccmFkbS9pbmRleC5waHB6XHgwN2FkbS5waHB6XHJhZmZpbGlhdGUucGhwelx4MGNhZG1fYXV0aC5waHB6XHgwZm1lbWJlcmFkbWluLnBocHpceDE2YWRtaW5pc3RyYXRvcmxvZ2luLnBocHpceDBiYWNjb3VudC5hc3B6XHgxMWFkbWluL2FjY291bnQuYXNwelx4MGZhZG1pbi9pbmRleC5hc3B6XHgwZmFkbWluL2xvZ2luLmFzcHpceDBmYWRtaW4vYWRtaW4uYXNwelx4MTRhZG1pbl9hcmVhL2FkbWluLmFzcHpceDE0YWRtaW5fYXJlYS9sb2dpbi5hc3B6XHgxNGFkbWluX2FyZWEvaW5kZXguYXNwelx4MTJiYi1hZG1pbi9pbmRleC5hc3B6XHgxMmJiLWFkbWluL2xvZ2luLmFzcHpceDEyYmItYWRtaW4vYWRtaW4uYXNwelx4MGVhZG1pbi9ob21lLmFzcHpceDE2YWRtaW4vY29udHJvbHBhbmVsLmFzcHpcdGFkbWluLmFzcHpceDFicGFnZXMvYWRtaW4vYWRtaW4tbG9naW4uYXNwelx4MTVhZG1pbi9hZG1pbi1sb2dpbi5hc3B6XHgwZmFkbWluLWxvZ2luLmFzcHpceDBjYWRtaW4vY3AuYXNwelx4MDZjcC5hc3B6XHgxOWFkbWluaXN0cmF0b3IvYWNjb3VudC5hc3B6XHgxMWFkbWluaXN0cmF0b3IuYXNwelxuYWNjZXNvLmFzcHpcdGxvZ2luLmFzcHpceDE1bW9kZWxzZWFyY2gvbG9naW4uYXNwelxybW9kZXJhdG9yLmFzcHpceDEzbW9kZXJhdG9yL2xvZ2luLmFzcHpceDE3YWRtaW5pc3RyYXRvci9sb2dpbi5hc3B6XHgxM21vZGVyYXRvci9hZG1pbi5hc3B6XHgxMGNvbnRyb2xwYW5lbC5hc3B6XHgwOHVzZXIuYXNwelx4MTBhZG1pbmNvbnRyb2wuYXNwelx4MGVhZG1pbnBhbmVsLmFzcHpceDBjd2ViYWRtaW4uYXNwelx4MTJ3ZWJhZG1pbi9pbmRleC5hc3B6XHgxMndlYmFkbWluL2FkbWluLmFzcHpceDEyd2ViYWRtaW4vbG9naW4uYXNwelx4MTVhZG1pbi9hZG1pbl9sb2dpbi5hc3B6XHgwZmFkbWluX2xvZ2luLmFzcHpceDFlcGFuZWwtYWRtaW5pc3RyYWNpb24vbG9naW4uYXNwelx4MGVhZG1pbkxvZ2luLmFzcHpceDE0YWRtaW4vYWRtaW5Mb2dpbi5hc3B6XHgwOGhvbWUuYXNwelx4MTNhZG1pbmFyZWEvaW5kZXguYXNwelx4MTNhZG1pbmFyZWEvYWRtaW4uYXNwelx4MTNhZG1pbmFyZWEvbG9naW4uYXNwelx4MWVwYW5lbC1hZG1pbmlzdHJhY2lvbi9pbmRleC5hc3B6XHgxZXBhbmVsLWFkbWluaXN0cmFjaW9uL2FkbWluLmFzcHpceDE1bW9kZWxzZWFyY2gvaW5kZXguYXNwelx4MTVtb2RlbHNlYXJjaC9hZG1pbi5hc3B6XHgxN2FkbWluaXN0cmF0b3IvaW5kZXguYXNwelx4MTZhZG1pbmNvbnRyb2wvbG9naW4uYXNwelx4MTRhZG0vYWRtbG9naW51c2VyLmFzcHpceDEwYWRtbG9naW51c2VyLmFzcHpcbmFkbWluMi5hc3B6XHgxMGFkbWluMi9sb2dpbi5hc3B6XHgxMGFkbWluMi9pbmRleC5hc3B6XHJhZG0vaW5kZXguYXNwelx4MDdhZG0uYXNwelxyYWZmaWxpYXRlLmFzcHpceDBjYWRtX2F1dGguYXNwelx4MGZtZW1iZXJhZG1pbi5hc3B6XHgxNmFkbWluaXN0cmF0b3Jsb2dpbi5hc3B6XHgxM3NpdGVhZG1pbi9sb2dpbi5hc3B6XHgxM3NpdGVhZG1pbi9pbmRleC5hc3B6XHgxMWFkbWluL2FjY291bnQuY2Ztelx4MGZhZG1pbi9pbmRleC5jZm16XHgwZmFkbWluL2xvZ2luLmNmbXpceDBmYWRtaW4vYWRtaW4uY2Ztelx4MTRhZG1pbl9hcmVhL2FkbWluLmNmbXpceDE0YWRtaW5fYXJlYS9sb2dpbi5jZm16XHgxM3NpdGVhZG1pbi9sb2dpbi5jZm16XHgxM3NpdGVhZG1pbi9pbmRleC5jZm16XHgxNGFkbWluX2FyZWEvaW5kZXguY2Ztelx4MTJiYi1hZG1pbi9pbmRleC5jZm16XHgxMmJiLWFkbWluL2xvZ2luLmNmbXpceDEyYmItYWRtaW4vYWRtaW4uY2Ztelx4MGVhZG1pbi9ob21lLmNmbXpceDE2YWRtaW4vY29udHJvbHBhbmVsLmNmbXpcdGFkbWluLmNmbXpceDBjYWRtaW4vY3AuY2Ztelx4MDZjcC5jZm16XHgxN2FkbWluaXN0cmF0b3IvaW5kZXguY2Ztelx4MTdhZG1pbmlzdHJhdG9yL2xvZ2luLmNmbXpceDEzbnN3L2FkbWluL2xvZ2luLmNmbXpceDEyd2ViYWRtaW4vbG9naW4uY2Ztelx4MTVhZG1pbi9hZG1pbl9sb2dpbi5jZm16XHgwZmFkbWluX2xvZ2luLmNmbXpceDE5YWRtaW5pc3RyYXRvci9hY2NvdW50LmNmbXpceDExYWRtaW5pc3RyYXRvci5jZm16XHgxYnBhZ2VzL2FkbWluL2FkbWluLWxvZ2luLmNmbXpceDE1YWRtaW4vYWRtaW4tbG9naW4uY2Ztelx4MGZhZG1pbi1sb2dpbi5jZm16XHRsb2dpbi5jZm16XHgxNW1vZGVsc2VhcmNoL2xvZ2luLmNmbXpccm1vZGVyYXRvci5jZm16XHgxM21vZGVyYXRvci9sb2dpbi5jZm16XHgxM21vZGVyYXRvci9hZG1pbi5jZm16XHgwYmFjY291bnQuY2Ztelx4MTBjb250cm9scGFuZWwuY2Ztelx4MTBhZG1pbmNvbnRyb2wuY2ZtelxuYWNjZXNvLmNmbXpceDE3cmNqYWthci9hZG1pbi9sb2dpbi5jZm16XHgwY3dlYmFkbWluLmNmbXpceDEyd2ViYWRtaW4vaW5kZXguY2Ztelx4MTJ3ZWJhZG1pbi9hZG1pbi5jZm16XHgwZWFkbWlucGFuZWwuY2Ztelx4MDh1c2VyLmNmbXpceDFlcGFuZWwtYWRtaW5pc3RyYWNpb24vbG9naW4uY2Ztelx4MGN3cC1sb2dpbi5jZm16XHgwZWFkbWluTG9naW4uY2Ztelx4MTRhZG1pbi9hZG1pbkxvZ2luLmNmbXpceDA4aG9tZS5jZm16XHgxM2FkbWluYXJlYS9pbmRleC5jZm16XHgxM2FkbWluYXJlYS9hZG1pbi5jZm16XHgxM2FkbWluYXJlYS9sb2dpbi5jZm16XHgxZXBhbmVsLWFkbWluaXN0cmFjaW9uL2luZGV4LmNmbXpceDFlcGFuZWwtYWRtaW5pc3RyYWNpb24vYWRtaW4uY2Ztelx4MTVtb2RlbHNlYXJjaC9pbmRleC5jZm16XHgxNW1vZGVsc2VhcmNoL2FkbWluLmNmbXpceDE2YWRtaW5jb250cm9sL2xvZ2luLmNmbXpceDE0YWRtL2FkbWxvZ2ludXNlci5jZm16XHgxMGFkbWxvZ2ludXNlci5jZm16XG5hZG1pbjIuY2Ztelx4MTBhZG1pbjIvbG9naW4uY2Ztelx4MTBhZG1pbjIvaW5kZXguY2Ztelx4MTJ1c3Vhcmlvcy9sb2dpbi5jZm16XHJhZG0vaW5kZXguY2Ztelx4MDdhZG0uY2ZtelxyYWZmaWxpYXRlLmNmbXpceDBjYWRtX2F1dGguY2Ztelx4MGZtZW1iZXJhZG1pbi5jZm16XHgxNmFkbWluaXN0cmF0b3Jsb2dpbi5jZm16XHgxMGFkbWluL2FjY291bnQuanN6XHgwZWFkbWluL2luZGV4Lmpzelx4MGVhZG1pbi9sb2dpbi5qc3pceDBlYWRtaW4vYWRtaW4uanN6XHgxM2FkbWluX2FyZWEvYWRtaW4uanN6XHgxM2FkbWluX2FyZWEvbG9naW4uanN6XHgxMnNpdGVhZG1pbi9sb2dpbi5qc3pceDEyc2l0ZWFkbWluL2luZGV4Lmpzelx4MTNhZG1pbl9hcmVhL2luZGV4Lmpzelx4MTFiYi1hZG1pbi9pbmRleC5qc3pceDExYmItYWRtaW4vbG9naW4uanN6XHgxMWJiLWFkbWluL2FkbWluLmpzelxyYWRtaW4vaG9tZS5qc3pceDE1YWRtaW4vY29udHJvbHBhbmVsLmpzelx4MDhhZG1pbi5qc3pceDBiYWRtaW4vY3AuanN6XHgwNWNwLmpzelx4MTZhZG1pbmlzdHJhdG9yL2luZGV4Lmpzelx4MTZhZG1pbmlzdHJhdG9yL2xvZ2luLmpzelx4MTJuc3cvYWRtaW4vbG9naW4uanN6XHgxMXdlYmFkbWluL2xvZ2luLmpzelx4MTRhZG1pbi9hZG1pbl9sb2dpbi5qc3pceDBlYWRtaW5fbG9naW4uanN6XHgxOGFkbWluaXN0cmF0b3IvYWNjb3VudC5qc3pceDEwYWRtaW5pc3RyYXRvci5qc3pceDFhcGFnZXMvYWRtaW4vYWRtaW4tbG9naW4uanN6XHgxNGFkbWluL2FkbWluLWxvZ2luLmpzelx4MGVhZG1pbi1sb2dpbi5qc3pceDA4bG9naW4uanN6XHgxNG1vZGVsc2VhcmNoL2xvZ2luLmpzelx4MGNtb2RlcmF0b3IuanN6XHgxMm1vZGVyYXRvci9sb2dpbi5qc3pceDEybW9kZXJhdG9yL2FkbWluLmpzelxuYWNjb3VudC5qc3pceDBmY29udHJvbHBhbmVsLmpzelx4MGZhZG1pbmNvbnRyb2wuanN6XHgxNnJjamFrYXIvYWRtaW4vbG9naW4uanN6XHgwYndlYmFkbWluLmpzelx4MTF3ZWJhZG1pbi9pbmRleC5qc3pcdGFjY2Vzby5qc3pceDExd2ViYWRtaW4vYWRtaW4uanN6XHJhZG1pbnBhbmVsLmpzelx4MDd1c2VyLmpzelx4MWRwYW5lbC1hZG1pbmlzdHJhY2lvbi9sb2dpbi5qc3pceDBid3AtbG9naW4uanN6XHJhZG1pbkxvZ2luLmpzelx4MTNhZG1pbi9hZG1pbkxvZ2luLmpzelx4MDdob21lLmpzelx4MTJhZG1pbmFyZWEvaW5kZXguanN6XHgxMmFkbWluYXJlYS9hZG1pbi5qc3pceDEyYWRtaW5hcmVhL2xvZ2luLmpzelx4MWRwYW5lbC1hZG1pbmlzdHJhY2lvbi9pbmRleC5qc3pceDFkcGFuZWwtYWRtaW5pc3RyYWNpb24vYWRtaW4uanN6XHgxNG1vZGVsc2VhcmNoL2luZGV4Lmpzelx4MTRtb2RlbHNlYXJjaC9hZG1pbi5qc3pceDE1YWRtaW5jb250cm9sL2xvZ2luLmpzelx4MTNhZG0vYWRtbG9naW51c2VyLmpzelx4MGZhZG1sb2dpbnVzZXIuanN6XHRhZG1pbjIuanN6XHgwZmFkbWluMi9sb2dpbi5qc3pceDBmYWRtaW4yL2luZGV4Lmpzelx4MTF1c3Vhcmlvcy9sb2dpbi5qc3pceDBjYWRtL2luZGV4Lmpzelx4MDZhZG0uanN6XHgwY2FmZmlsaWF0ZS5qc3pceDBiYWRtX2F1dGguanN6XHgwZW1lbWJlcmFkbWluLmpzelx4MTVhZG1pbmlzdHJhdG9ybG9naW4uanN6XHgxMWFkbWluL2FjY291bnQuY2dpelx4MGZhZG1pbi9pbmRleC5jZ2l6XHgwZmFkbWluL2xvZ2luLmNnaXpceDBmYWRtaW4vYWRtaW4uY2dpelx4MTRhZG1pbl9hcmVhL2FkbWluLmNnaXpceDE0YWRtaW5fYXJlYS9sb2dpbi5jZ2l6XHgxM3NpdGVhZG1pbi9sb2dpbi5jZ2l6XHgxM3NpdGVhZG1pbi9pbmRleC5jZ2l6XHgxNGFkbWluX2FyZWEvaW5kZXguY2dpelx4MTJiYi1hZG1pbi9pbmRleC5jZ2l6XHgxMmJiLWFkbWluL2xvZ2luLmNnaXpceDEyYmItYWRtaW4vYWRtaW4uY2dpelx4MGVhZG1pbi9ob21lLmNnaXpceDE2YWRtaW4vY29udHJvbHBhbmVsLmNnaXpcdGFkbWluLmNnaXpceDBjYWRtaW4vY3AuY2dpelx4MDZjcC5jZ2l6XHgxN2FkbWluaXN0cmF0b3IvaW5kZXguY2dpelx4MTdhZG1pbmlzdHJhdG9yL2xvZ2luLmNnaXpceDEzbnN3L2FkbWluL2xvZ2luLmNnaXpceDEyd2ViYWRtaW4vbG9naW4uY2dpelx4MTVhZG1pbi9hZG1pbl9sb2dpbi5jZ2l6XHgwZmFkbWluX2xvZ2luLmNnaXpceDE5YWRtaW5pc3RyYXRvci9hY2NvdW50LmNnaXpceDExYWRtaW5pc3RyYXRvci5jZ2l6XHgxYnBhZ2VzL2FkbWluL2FkbWluLWxvZ2luLmNnaXpceDE1YWRtaW4vYWRtaW4tbG9naW4uY2dpelx4MGZhZG1pbi1sb2dpbi5jZ2l6XHRsb2dpbi5jZ2l6XHgxNW1vZGVsc2VhcmNoL2xvZ2luLmNnaXpccm1vZGVyYXRvci5jZ2l6XHgxM21vZGVyYXRvci9sb2dpbi5jZ2l6XHgxM21vZGVyYXRvci9hZG1pbi5jZ2l6XHgwYmFjY291bnQuY2dpelx4MTBjb250cm9scGFuZWwuY2dpelx4MTBhZG1pbmNvbnRyb2wuY2dpelx4MTdyY2pha2FyL2FkbWluL2xvZ2luLmNnaXpceDBjd2ViYWRtaW4uY2dpelx4MTJ3ZWJhZG1pbi9pbmRleC5jZ2l6XG5hY2Nlc28uY2dpelx4MTJ3ZWJhZG1pbi9hZG1pbi5jZ2l6XHgwZWFkbWlucGFuZWwuY2dpelx4MDh1c2VyLmNnaXpceDFlcGFuZWwtYWRtaW5pc3RyYWNpb24vbG9naW4uY2dpelx4MGN3cC1sb2dpbi5jZ2l6XHgwZWFkbWluTG9naW4uY2dpelx4MTRhZG1pbi9hZG1pbkxvZ2luLmNnaXpceDA4aG9tZS5jZ2l6XHgxM2FkbWluYXJlYS9pbmRleC5jZ2l6XHgxM2FkbWluYXJlYS9hZG1pbi5jZ2l6XHgxM2FkbWluYXJlYS9sb2dpbi5jZ2l6XHgxZXBhbmVsLWFkbWluaXN0cmFjaW9uL2luZGV4LmNnaXpceDFlcGFuZWwtYWRtaW5pc3RyYWNpb24vYWRtaW4uY2dpelx4MTVtb2RlbHNlYXJjaC9pbmRleC5jZ2l6XHgxNW1vZGVsc2VhcmNoL2FkbWluLmNnaXpceDE2YWRtaW5jb250cm9sL2xvZ2luLmNnaXpceDE0YWRtL2FkbWxvZ2ludXNlci5jZ2l6XHgxMGFkbWxvZ2ludXNlci5jZ2l6XG5hZG1pbjIuY2dpelx4MTBhZG1pbjIvbG9naW4uY2dpelx4MTBhZG1pbjIvaW5kZXguY2dpelx4MTJ1c3Vhcmlvcy9sb2dpbi5jZ2l6XHJhZG0vaW5kZXguY2dpelx4MDdhZG0uY2dpelxyYWZmaWxpYXRlLmNnaXpceDBjYWRtX2F1dGguY2dpelx4MGZtZW1iZXJhZG1pbi5jZ2l6XHgxNmFkbWluaXN0cmF0b3Jsb2dpbi5jZ2l6XHgwY2FkbWluX3BhbmVsL3pceDEwYWRtaW5fcGFuZWwuaHRtbHpceDA3YWRtX2NwL1x4ZGFceDAwejFceDFiWzE7MzQ7NDBtW1x4MWJbMTszNzs0MG1URVJFWFx4MWJbMTszNDs0MG1dPlx4MWJbMTszMjs0MG0gelx4MGMgXSA6OiBGb3VuZCB6MVx4MWJbMTszNDs0MG1bXHgxYlsxOzM3OzQwbVRFUkVYXHgxYlsxOzM0OzQwbV0+XHgxYlsxOzMxOzQwbSB6XHgxMCBdIDo6IE5vdCBGb3VuZCApXHgwN1x4ZGFceDA2dXJsbGliWlx4MDdyZXF1ZXN0Wlx4MDd1cmxvcGVuXHhkYVx4MDVwcmludFpcdEhUVFBFcnJvclpceDA4VVJMRXJyb3JceGRhXHgwNGV4aXQpXHgwNlpceDAzdXJsWlx4MDh1cmxfb3BlblpceDA2YWRtaW5MXHhkYVx4MDFpWlx4MDRDdXJsXHhkYVx4MDNtc2dceGE5XHgwMHJcblx4MDBceDAwXHgwMHJceDA0XHgwMFx4MDBceDAwXHhkYVx4MDVBZG1pbihceDAwXHgwMFx4MDBzKFx4MDBceDAwXHgwMFx4MDBceDAxXHgwNFx4MDFceDA0XHgwMVx4MGNceDAxXHhmZlx4MDBceGZmXHgwMFx4ZmZceDAwXHhmZlx4MDBceDg4XHgwMVxuXHgwMVx4MGVceDAxXHgwMlx4MDFceDBjXHgwMVx4MThceDAxXHgxNFx4MDEkXHgwMVx4MTZceDAxXHgwOFx4MDFceDFlXHgwMVx4MDZceDAxclx4MGJceDAwXHgwMFx4MDBhXHg5YVx4MDRceDAwXHgwMFx4MWJbMTszNDs0MG1cbiAgICAvJCQkJCQkJCQgLyQkJCQkJCQkLyQkJCQkJCQkJCAvJCQkJCQkJCQgLyQkICAgLyQkXG4gICB8X18gICQkX18vfCAkJF9fX19fL3wgJCRfXyAgJCR8ICQkX19fX18vfCAkJCAgLyAkJFxuICAgICAgfCAkJCAgIHwgJCQgICAgICB8ICQkICBcXCAkJHwgJCQgICAgICB8ICAkJC8gJCQvXG4gICAgICB8ICQkICAgfCAkJCQkJCAgIHwgJCQkJCQkJC98ICQkJCQkICAgIFxcICAkJCQkLC9cbiAgICAgIHwgJCQgICB8ICQkX18vICAgfCAkJF9fICAkJHwgJCRfXy8gICAgID4kJCAgJCRcbiAgICAgIHwgJCQgICB8ICQkICAgICAgfCAkJCAgXFwgJCR8ICQkICAgICAgIC8kJC9cXCAgJCRcbiAgICAgIHwgJCQgICB8ICQkJCQkJCQkfCAkJCAgfCAkJHwgJCQkJCQkJCR8ICQkICBcXCAkJFxuICAgICAgfF9fLyAgIHxfX19fX19fXy98X18vICB8X18vfF9fX19fX19fL3xfXy8gIHxfXy9cblxuICAgICAgXHgxYlsxOzMwOzQwbVtceDFiWzE7Mzc7NDBtK1x4MWJbMTszMDs0MG1dICAgICAgXHgxYlsxOzM0OzQwbUZhY2VCb29rIFx4MWJbMTszMTs0MG06IFx4MWJbMTszNzs0MG1BYmR1bHJobWFuQWx3c2FieSAgICAgIFx4MWJbMTszMDs0MG1bXHgxYlsxOzM3OzQwbStceDFiWzE7MzA7NDBtXSAgIFxuICAgICAgXHgxYlsxOzMwOzQwbVtceDFiWzE7Mzc7NDBtK1x4MWJbMTszMDs0MG1dICAgICAgXHgxYlsxOzM0OzQwbVRlbGVHcmFtIFx4MWJbMTszMTs0MG06IFx4MWJbMTszNzs0MG1BYmR1bHJobWFuQWx3c2FieSAgICAgIFx4MWJbMTszMDs0MG1bXHgxYlsxOzM3OzQwbStceDFiWzE7MzA7NDBtXVxuXG4gICAgICAgLS0tLS0tLS0tLS0tPT09PT09XHgxYlsxOzM0OzQwbVtceDFiWzE7Mzc7NDBtVEVSRVhceDFiWzE7MzQ7NDBtXVx4MWJbMTszMDs0MG09PT09PT0tLS0tLS0tLS0tLS1cbiAgICAgICAgICAgICAgICAgICAgIFx4MWJbMTszMTs0MG09PT09PT09PT09PT09PT1cblxuXG5ceDFiWzE7MzQ7NDBtVEVSRVgucHkgXHgxYlsxOzM3OzQwbS11IFx4MWJbMTszMDs0MG18fCBceDFiWzE7Mzc7NDBtLS11cmwgXHgxYlsxOzMxOzQwbSsgXHgxYlsxOzM3OzQwbXVybCBceDFiWzE7MzE7NDBtKyBceDFiWzE7Mzc7NDBtL1xuXG5ceDFiWzE7MzE7NDBtZXg6XG4gICAgIFx4MWJbMTszNDs0MG1URVJFWC5weSBceDFiWzE7Mzc7NDBtLXUgXHgxYlsxOzMwOzQwbWh0dHBzOi8vd3d3Lmdvb2dsZS5jb21ceDFiWzE7Mzc7NDBtL1xuXHgxYlsxOzMxOzQwbW9yOlxuICAgICBceDFiWzE7MzQ7NDBtVEVSRVgucHkgXHgxYlsxOzM3OzQwbS0tdXJsIFx4MWJbMTszMDs0MG1odHRwczovL3d3dy5nb29nbGUuY29tXHgxYlsxOzM3OzQwbS9cbnpceDAyLXV6XHgwNS0tdXJsXHhkYVx4MDNvX3UpXHgwMVpceDA0ZGVzdFx4ZGFceDA1Y2xlYXJceGRhXHgwMVxuKVx4MWFaXHgwZXVybGxpYi5yZXF1ZXN0clx4MDVceDAwXHgwMFx4MDByXHgwMlx4MDBceDAwXHgwMFpceDA4b3B0cGFyc2VaXHgwNnJhbmRvbVx4ZGFceDAyb3NceGRhXHgwMWJceGRhXHgwMXJceGRhXHgwMXdaXHgwMnJhXHhkYVx4MDFnWlx4MDJiblpceDA2YmFubmVyXHhkYVx4MDFwWlx4MDZjaG9pY2VyXHgwNlx4MDBceDAwXHgwMHJceDBiXHgwMFx4MDBceDAwWlx4MGNPcHRpb25QYXJzZXJceGRhXHgwMVhaXG5hZGRfb3B0aW9uWlxucGFyc2VfYXJnc1pceDA2b3B0aW9uXHhkYVx4MDRhcmdzclx4MGNceDAwXHgwMFx4MDBceGRhXHgwNnN5c3RlbVpceDA1dXNhZ2VyXG5ceDAwXHgwMFx4MDByXG5ceDAwXHgwMFx4MDByXG5ceDAwXHgwMFx4MDByXHgwNFx4MDBceDAwXHgwMFx4ZGFceDA4PG1vZHVsZT5ceDAxXHgwMFx4MDBceDAwczJceDAwXHgwMFx4MDBceDA4XHgwMVx4MGNceDAxXHgwOFx4MDFceDA4XHgwMVx4MDhceDAzXHgwNFx4MDFceDA0XHgwMVx4MDRceDAxXHgwNFx4MDFceDA0XHgwMVx4MDRceDEzXHgwNFx4MDNceDEwXHgwMlxuXHgwMlx4MDhceDAxXHgwOFx4MTNceDAyXHgxN1x4MDZceDAyXHgxMFx4MDFceDBjXHgwMVxuXHgwMVxuXHgwMVx4MGNceDAyXG5ceDAxXHgxMFx4MDEnKSkK'
exec (base64.b64decode(Golde))
