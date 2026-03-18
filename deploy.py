#!/usr/bin/env python3
"""
Deploy script for Budget3DPrint.
Uploads the public/ folder to a web host via FTP or rsync.

Configure the variables below before running.
"""

import os
import sys
from pathlib import Path

# ── Config (fill these in once hosting is set up) ─────────────────────────
FTP_HOST = 'your-host.com'        # e.g. ftp.namecheap.com
FTP_USER = 'your-ftp-username'
FTP_PASS = 'your-ftp-password'
FTP_REMOTE_DIR = '/public_html'   # root directory on host

PUBLIC_DIR = Path(__file__).parent / 'public'


def deploy_ftp():
    """Upload all files in public/ to FTP host."""
    import ftplib

    print(f'Connecting to {FTP_HOST}...')
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.set_pasv(True)
    print('Connected.')

    def upload_dir(local_dir, remote_dir):
        # Ensure remote dir exists
        try:
            ftp.mkd(remote_dir)
        except ftplib.error_perm:
            pass  # already exists

        ftp.cwd(remote_dir)

        for item in sorted(local_dir.iterdir()):
            if item.is_file():
                print(f'  Uploading {item.relative_to(PUBLIC_DIR)}')
                with open(item, 'rb') as f:
                    ftp.storbinary(f'STOR {item.name}', f)
            elif item.is_dir():
                upload_dir(item, f'{remote_dir}/{item.name}')
                ftp.cwd(remote_dir)

    upload_dir(PUBLIC_DIR, FTP_REMOTE_DIR)
    ftp.quit()
    print('\nDeploy complete.')


def build_and_deploy():
    """Run build then deploy."""
    os.system('python build.py')
    deploy_ftp()


if __name__ == '__main__':
    if FTP_HOST == 'your-host.com':
        print('ERROR: Configure FTP settings in deploy.py before running.')
        print('You need: FTP_HOST, FTP_USER, FTP_PASS, FTP_REMOTE_DIR')
        sys.exit(1)

    build_and_deploy()
