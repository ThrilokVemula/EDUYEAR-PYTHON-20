from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
	data=[
	{
	'url' : 'https://images-na.ssl-images-amazon.com/images/I/61KZfvvD6hL.jpg',
	'title': 'Physics Book',
	'desc' : 'Author: Clifford A.Pickover Edition:2 Book Id:101'
	},
	{
	'url':'https://imgv2-2-f.scribdassets.com/img/word_document/431782167/original/216x287/d5e719aea8/1617225635?v=1',
	'title':'The Chemistry Book',
	'desc':'Author:Derek B.Lowe Edition:9 Book Id:102'
	},
	{
	'url':'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVFRgVFRUYGBgYGBoYGBoYGBgYGBgZGBgcGRoYGBgcIS4lHB4rIRgYJjgmKy8xNTU1GiQ7QDs0Py40NTEBDAwMEA8QHxISHjQrJSs0NDQ0NDQ0MTQ0NDQ0MTQ0NDQ0NDQ0NDQxNDQ0MTQxNDQ0NjQ0NDY0NDQ0NDQ0NDQ0NP/AABEIAPwAyAMBIgACEQEDEQH/xAAbAAABBQEBAAAAAAAAAAAAAAAAAQIDBAUGB//EAEMQAAIBAgQCBgUKBgEDBQEAAAECEQADBBIhMQVBEyIyUWFxM1KBkbIGFCNCU3KSobHRFWJzweHwgiRD8TRjg5OzFv/EABgBAAMBAQAAAAAAAAAAAAAAAAABAgME/8QAJhEAAgICAgIBBAMBAAAAAAAAAAECERIxAyEyUUETImHBcYHwBP/aAAwDAQACEQMRAD8A87xDnO4n6x/U1W6Q99Wbiz0h5htO/Vqo02+2OqSJjdkCaYH1pMvl7xU+CwD3nW3bUszbdwHNmPJfGgRLw/CvedbdtSzsfYBzZjyA767nB8HTDFkBzOCVZ+Zg6x3DTatn5PcBTCpC9Z27b8ye4dyjkKj4l6V/vt+tdHDFWc/NLror5zyJ99O6ZvWb3mo5orqo5rJBiX9dvxGnfO39d/xN+9QTS0YoLZOMXc9d/wAbfvThjbv2j/jb96rTS0sUFss/Prv2j/jb96X57d+0ufjb96rUUqQ7ZaGOu/aP+Nv3pfn1z7R/xt+9VhTqMUO2TjG3PtH/ABt+9Hz259o/42/eq9FGKDJk3zu567/ib96b86f13/EajpKMUO2SHEP67e803pm9Y+802m0YoVjzcPeaQu3eaSaa5oodlnCYrK6k7TB8jofyNFU5opYhZ5tdPWbzP6moKnujrN5mlwWEe6627a5nY6DlHMseQHM1wPZ3fAmBwb3nW3bXM7GAOQ7yx5Ad9etfJ7gSYVABDOQM7xBaOQ7lE6Ck+TfAEwqQOs7RnuRqT6q9yju9prYrSMaM5SsDWJxT0tz75rbNYnFPS3PvGtuLyMOTRTpaKK6TESloiiKACnCkpQKAFFJTqKQCilpBSigYUUUUAFJS0lACUUtJQA2mtUlMagYwCinCipA88s4N7t3o7YLMxPkBzJ7gO+vT/k5wFMKkDrO3beN/5V7lHdUHyT4Ulm1nGr3BLMRrHJR3CugrjUa2dcpWKKKSiqICsXinprn3v7CtqsbivpX8x8IrXi8iOTxKdUb3FbSXBaZjnbKAIMS2wJ/3er1cViLfSJfxI7S3lKfdTTTwhlP/ABrScnHRnCKls7WoDjF6QWZOcrnAjTLMb+ys7ifE2yWRZgPfIyk6hQQCTHf1h+dU7Nu6uMVXdWfoWCuq5dJMErtIM/lQ590gUOrZ0sU4VzX8YufNSxI6cXOi2HbzTtEdmrnE3urknEW7KhBLsoLu436p0jyp5qrQYOzZFLXMfxm6cG13MA6vkzACCJGsHTY1M2KxFu/ZD3FZbxIKKgATQbNue0NfOl9RDwZ0Qpa5xcRicQ902bgRLTFFUqrZ2XeSdp0940o4txS4htWmdbLMua64GcLGwUEcyD+VLNVYYO6OjqpjselnIWDddwgygHrNtMnbSsDD/KBlt35dbptZcjhYDhzlGZR3H/edQcSs3wmHe9dz57ts5cgBViJ0YbiJG1J8nXRSh32dhRSmkrUyEoNLSGgY2kNPppoAbRThRUDNPgnoE+7/AHNX6ocB9AnkfiNaArmltm6EpaKKACsbi3pX9nwitmsfi3pX/wCPwLWvF5EcniZeOL9G+QS+UhRoNSIGp08axcH8mLRtrnVg+XrdbZjy000/tXQ0orVxjJ2zJSaVI5e3w3ECzaOSLlhyVUlYdCQ2hBjfTXkKt4WziGxCXrloIuRkgOGK7kZvMnlW9RQuNL5G5t/Bz78Ic4vPH0OcXTqO2FiIme1rtzpcXhLy4lrq2kuhlVULsFFuN9DrvO3fW/ToowX7DN/o5YcHv/M3tZBnNzMBmWCJXUGYGx3rT4jgne7hnVZFtiXMgQOr3nXY7Vr0tJQWgzZzowuJsNdFlFdLrF1YsFKM28gnWP7CpMdw+/ms31CXLiKVddFVgZ7M6CJP5Hwreoo+mvYZsxGwN6/ZureVEzxkVdSuWCMzDcSB+flVO9g8XdW0jogFp0ac4LPl0zaaDSa6eihwTGptAaSloqyBKDRFFACU0040kUDEWihTrRUjNH5P+gTyb42rRrN+TvoLf/L42rUrlltm60JRRRQAVj8X9K3kvwLWzWNxf0reSfAtacWyOTxKVcdwfDi6hZ8S6EMVjpI0ABnrHxPursa4rgqYQo3zjLnzkCS46uVY7J781XybX9kw0zozfTC20V3dgWIDt1jqS0se4T+VSYHi9u65RQ6sBmAdcuZe8e8b1m8bxCOMMyMGXp1EiY0MRrU17/16f0T+rUZNOloMU1b2S3PlFZBOjlFJBcJKZh9UNO9Kl9GxFsk3VdrMhGgKAS2rj1t/cK5zCPntHD9Nbt2i50uSLoUNIB+ryHP9q3LkfP7UbdBp5S9SpN7G4paJn+UtkZoW4xUkMFWcoBjMxmAN+fKrWJ4tbREfrMHjIqLLvInRf3rE4aP+mxf37vwCq14QuCcuUTIy5xHUY7b9/wCgPdTzlQYxs6XB8Xturt1kNvV1cZWQRMkd2hqDCcetuyrluIH0RnSEf7pn9ax7uHV1xLW773n6NQ+gggMraMohjCkQKTDLZcWA2LdjmQogCtkdRoCAJUaRP/mjOQ8Im1c4/aW4bJV84dUGgglvrDXsjnUGAxlq2mJdelYJdbOGyk5s0EJr2fOm8GUfO8UYEgpB5iQZj3D3Vm2/QY/+q/x0snsElr+DYt/KK2WUZLgVyFVykJmPKZ110kfprUmN40qOba23uMgzPkAOQHXXXeDNZfFj/wBPg/v2fgqDiGK6PFXstwWc6oGLozhjl7SwDEDv5zQ5tAoJnR8Mx4voXVGVZIUtHWA+sANtZHsq4az+BW7aWES24dVnrDmxMnTlqdq0Ca1i3XZnKr6EoiiaJoEKBRQppaQy38nT9Anm/wAbVqCsv5OegTzf42rUiueS7ZutBRS0lKgCax+MelbyT4FrYrH4x6U/dT4FrTiX3EcniUZqp/C8P9jb/Av7VbrF4Nxw33KMgQ5SywxMwYPId/61tLG0mYpOm0aa4O0Aqi2sK2ZRlWFb1lEaHxp9zDqxzZQHylQ8DOoPcd+dZV/jZXECwEBBZVLZjoWE7R4itmhYvQ2mtnNLwa/kNrJh2mfpWzF+sdW1E5v98a3sHgVRUGUFkQIHKjNAGwO4G+njUfFMeLCBypaXCQDG4Ov5U3G48petW8oIuFpMwVygHQc96SUYjblItrhkAZQigNJYBQAxO5Yc5obDqVyFFKbZcoy+WXapRRVUTYyxZVBlVVQdygKPcKS1hLasWW2qsd2VFBPmQKkp00qHbGraUEsFALdogAEx3nnTRYSGGRYYywyiGPe3fUhqO/dyIz75VLb7wJiaKEK1pSACqkDYECBG0DlWLc4ZfW5ce21phcMnpVYsscgRy1/SrVviD3MOL1pAWOyMwjt5TLacgTWgrdUFoGgnXQHnrU0pFW4lLg/D+gRlLBmdy7EDKsmBCjkNKvmiedNVwRIII8DNUlSpCbvsU0URRToByb0Utsa0VDKRc+TfoE83+Nq1RWV8m/QL5v8AG1a4rCXkzZaG0RRTopANisfjA+lP3U+Ba2orG4z6U/dT4FrXi8iOTxM+K4zAno1sXuQvPbf7r9/l1jXa1jDgX/TtYL7vnDZdjIO0+Eb860nFvtGcJJbMbDKS1i6d7uJd/wDjKgD8jV3jFu09xxlu3XVR1UaFtabzoATvGu1aT8IBGHAeBYIO3bgDx0mPzqG5wVs7sl9kS7q6hVJO+zHbc++oxaVUVkm7sxMYmfB2bjEs6uUBJPZLMNe89VdavcUwCLdwtpSyrNwSGOYTBMNvzPvq83Apwww+fVWzB8vPMT2Z/mI3qUcKYtZd7uZ7Rck5QM+Y6DQ6QIFGL9eh5L37Mqwvze9iUtyFWznCkk9YKDOvmapYbD3CiXLdm6bshulzghtdQVJ2O1dQOGjpnulpDpkKRpGgOs+HdzqnZ4E6woxDi0rZggADaGYzgzE0ODBSRVfBJextxHzZejRioYqCQEAmNwJrPscPR8NddizG0zqkscqBYOi7aya6m1w/LiHv5u2gTLG0Zdc069nu51DZ4OFs3LWeekZmzZezmjSJ12owv49iU6+TOxL23s4ZbouXHZFYIhMucgkv4DeZ7/GqnDcOGXF2mVkRQrqhecjAMw6wOuqr7q17vAzFopdZHtJkDhQcyxHZJ0O/vqXAcGFs3SXZ+lADZozaAyZ59o8qMW32h5JLp/6znRhFXh73AOs+XOZJnLehdNhvyq/esi/iLVm5JRbCvlkgMxESY9nuq1b+T5Fl7DX2KNlyjIBkyvnMa6yas43g4fIyuyOihA6jdQIgj3+80KLpdA5K9lTGcFK4d7VlmOZwwRm0yzqinkPM/rTeAtaDugstZuZQWQklSB9ZZ8x/bnVpOBqLbIbjlnYOz5iGzjY+Xh/iJcDwrI5uPce45XICwAhZmABTp2mkLJU1ZfoinUVqZi29xS0toaiis5PstFz5OD6FfvP8bVq1lfJv0K/ef4zWuawl5M2WhEQnYE+QmndC3qt7jWD8r7pXDKQSPplGhI+o9cQcW/rt+I/vVx48ldibo9V6F/Vb3Gsri2EuG4SqORlTUKxGiDwrz04p/Xb8RppxDesfea0jx4u7IlLJVR3HzG79m/4G/aj5hd+yf8DftXDfOG9Y+80dOe8+81pT9kYo7r5hd+yf8DftSfMLv2b/AIG/auF6Y9599HS+NOn7Fiju/mF37N/wN+1L8xu/Zv8AhNcH0lTW3kRz3H96TtfI1FHb/Mbv2b/hNHzG56je41x9okid45U8Nrp4kft/v96zcmUoo6i7aZDDKVMTqOXf+RptJb9FZ/pn/wDR6Wri7VmclToKKKKYhKJopDQAtJNFNoGOoptFAE1gnMsd4/WijDdtPvL+oorKezWOi38mvQL95/jNa9cfw3jDWkyBAwBYySRuSdvbWlY+UM6MgHtJrOSeTLvoj+XOmGX+unwXK8/zV2fywxRfCgnLpiEjKe+3d3nauEL04yx6Kq+yfPSF6rl6OkqsxYljPQXqqXpc1GYYlnPR0lVc9GenmGJa6SpsNLMAu9UFadK17drIMn1zBY+qDsPfHtNTKYYllturou5Oupnbw8TyqJr0yPaD/nu/ahYaUUkKCJO06ajfftfkKie5m0H1Y225CB4aTUKQNHX4R5sWD/7Z/K64qQVjX+IPbtYcJlg23OoJ/wC/c03qt/GbncvuP710w7iYyX3HRUlc9/Gbn8vuP70n8Yufy+7/ADVURTOipK57+L3P5fd/mk/i9z+X3f5ooMWdBRXPfxe5/L7v80fxe5/L+Gih4s6Giue/i1zvX3U4cUud491KhqLOmwfbT76/qKKx+F8Rc3bYJGroNu9hRWctmkY9DsAquCp0YFoPmae+Ggw2njyP7Gq2GU7jeT+tbNi4HENvUvtiMXjyN80y6ycTbAH/AMV6speHWwsu0ZQS5G/lvvyFdNxrDsMMQqlyL9sqIJ/7dwcgZ37q5PiNm6LYGRhm6zdUiApgAzHPXUd1c83Umjoh4oyb1wEkgQOQ7hURap/mVwxCGTA9p2H608cKvGOode+B/u9RkUVM1Garf8Ku9y7gdpeex321o/hNznkGsdtaeQFTNV5OGvALlUB9doP4RLflWjw7h2QnMQpVmVn8VYKQk7ee/lVxcoVciHkC56s9U6ydWFGTAzcJhQhkEO5JRAAw60bjMBPL86mVTmFtG6zgB32Alu+dtFjzPfo69cZXYqoznKwYEgqCDmLSPAe7xpl0ZZspDMHOZ/aFEctTB01kjmKMhURrcBhEgZVOYnUgMVkHlMwP/JpbElgiDXTyBPMnvp1vDdY27REELJjTrKDJnY6tA7oqwyBUyKDObKTzDq5lie/qju3PMaGQUWuKJlt4de624PmL9wEHxmalw+ARrYcq05CZ6xk51BYBfqgNv7DESW8Wul7eGZono3B8SLrifOsqK7YW4o55dSZvDh1sZi6MgXpCevJ6mTKPAsGdtdTl00pl/hqK1tYMM6ITm0cM7q0eQRNvX8qxaKqn7JtejaTAJlDMhU9XQllzTdZGENqIVV/HrypyYCzGYqYhmMMdCpQBB5hnOuvU8DWHFJRT9jv8E+OshHZFMgRqNQeqCSPbUFFKKpAFOWkpy0hUaHCfTW/vp8Yoo4T6a3/UT4xRWU9mkdFnCaHXYk/rWgixt7DVPBpmBHeWI85q9htRlNJ7JF4sM+GVf/fQRrJ6lzQQrVz2NSGyDVVEQFeAqAMZ6g3PhuD411dyzmsGeV1DGuvUcf38da5S7ZKBiQmnZIaQY1LE8wXIjauXk8mbw8UUGAZ4zZSoOpAaCTk+sQT2nbymppAgm4sqhYjKinMdW+voddu8VLhuGFh18kswABuMdoA2eZ1fQ8wKtjAKSxBTVgsyTMNqO3zUr5VmUZ1sJ1B0nfsUGgPVMB+4AiPCm2Spyy7jM6ntrzAnYkbyPZWmvDRI6ySqfZudVBnnoIIMeEUtnhYDJ2e0CIsnSHnTTTQET4zQMYhQOSwzkvcyqBO7iDHtmaa/SMknKgkCAAzGGy6yY2FTJbbU21DscxImIBIM66kCDUN3CuVLO5Ak6AhF0f1m1O3dVMRQxQcMMhYlkIknQZGDTAWJGWd+VOt2yrdDZOZ3QZzA6rGGMg6EjLp5mlvWklCroGzlQQXcgERMjTc91R3HW0qok9IpbMR1zJykE9xHWXyJ76EBLh8RaRMmuZlLTzzgq9tyNxBEQO9qaUIGzBT1tZBYLlLAc82VpA5x71wuACo7OcrqGME5srwrISpE7MD7DUd287oqL1UVmM7mGJICzr9YgHegDT4rl6PD5dstznpPTvmj+WZgchArLrR4hYCWMKqmRkuEHvzXWb361nV38Xijmn5MKKKStCBTSUTRQAUtJRNBQ8Uq0ynoaQGjwn01v+onxiik4T6a3/UT4xRWU9mkdGjgk6o82/U1cZdmHt/3xpmASbYPi3xmKnt9x50nszJ7rzhmiZzoNMsnqvsW0B/auexGGOYCJAIBJCAwu5zEHct+VbWMXLhySubLeQxlVtcjwQCDGsGRXO2UYTCM2y6qDEsSSep3yPKuWa+5nTDxRp2mKjtv1V+0BDTIAMJqDm38R3VGXEQX2UuSb2uVUIMnJqIM+dR9M+WBbKywUaEEAHfVdNTTPnNwZ2CkEHq6iN4bQsI2/XxqKLLLuCSOr1lMfSH6w8IjsgzvvTUZcyNC6dY9d2iHQnTNqJA/2ahxGIvAsCIyKIllHZEc37t/M0hvXhzGn8y84Mdv20UBPgtdMunrDcE5dQN+7WeVWLOFRlJ6TNmD9vK2XXYAgHv3NVsDnjqETI3kg6DxkVbt2wTLqTMiJBB0EwG/ahgkZ/EcJ9CLlsrGjPlUDLB3GRTIOh3rKFhLa3Gc5mOQp4hoZ1CjvRgJ8TXXcPtjowmUADMgldNe0jLtGtYWM4QTeEZlQmBp2IE5SRoRpHtAoTQmjLtX3uswaewB1lAjLrLEazEn21r/ADfoih0O9pyRM6B7Zk8iMyVRbEpaCoIDK8gZQdCmUqfaz6+AoxzvrqZG5Go6okEg7SKqibJcekYfCiSYW4AW7UdId/HlWdWhjFjD4bWZ6YjfY3JEz51nzXdxeKOefkwNJFLSVqQEUUURQAUUUUFC09aYKetJgaHCfTW/6ifGKKOFelt/1E+MUVjPZpHRv8KXqL3Et8ZqZ0g/77KZwn0Q82+NqtOsiaHszKXFSDhoaY6dJgTICOYP6Vh2bQEHeAW7BmTBOs79kxXQcQ/9PGsm+g0+49Y1u3v1rnWI5GYj7+g194rnntm/HpEpM5Vjlm7BgZjIM+ag+6oUBgdQy5k/RnYjKZ/EfcakuKCW7fd2fW6piT3qDSLllZD6S2oUasc2vjKj31nRoNvsxLkoxlj9TeV8dxSM7Seq0QNYUDQFe7u1qIhBHVbVp3Qaq+YctusfYKRymojbTtp9XOBy8aeIWS4e8oIBJB5HvPV0zARVgdNPVcQD3DuPqkmapW7wUaiNRrEqTpvFIyqZjLBOsGPynx7qTiJM1+HhwWlpIJLJDQRJ7ObWR4VJiCIjMYG3KYMlWPI9UflWdgiquQ0iSIYGSpA0P61pMh2yglgfuuN58GrOXTNI9o5zG4YhoCggadY66HnEGffToBAOxjWNesv+Km4naBgnUwO1AII6uU7a6VHhHIBHMEQCZ05xI8q6ErjZjLp0O4kmWxhwdY6b3Zwf71lxWzxgfQ4fzvfGutQ4Xgty4iuuXK3SbkiOjEnNppOw/tXXxtKKswkrl0ZkURV5OGXGcIFOromfK4QM4UqGYrp2h/monwVwZptuMpAYlGhS0ZQdNJkR3yKu0KmV4oird3AOiF3UrD5CrAq4JXOOqRtFWMbwe5bMQHgNmyZmCFDlcNppB57eNK0FMy4oy1cbA3BmBtuMoBaUYZQdi2mgPjUo4Xdyu2RhkylgVYNDZusBHZGRpPKnaCmUAtOUVYODueo/Zzdhuzybbs+O1FzDshh0ZTvDKVMd8HyNFodE/C/S2/vp8QopcBo6ffX4hRWM9lI6PhWiDzf42q6N4qjwvsDzb42q81BmyHH4F7lnKgki6rHVRpkZZ1YetWQPk7d06o/Hb0n/AJ1uOJFVmEf77qmn8MpSXoyD8nbsaqkk+vaHL7/fUn/89ck9iIj0lnu+9/sVpusiffRbfv5aH+xop+x5r0ZI4A+no9N/prGk699NbgDwZNvfWb1nu/fSta8kaj/fCoW8P/I9Xz7vdRTDP8ENrg7qD17Y1+1txy3g+Hcarvg053cN/wDdbH6EVPngiNuXiPVP9vdXKtvRHiTd2V9R1VHUYawiMfpcMVICkdMu3tJq1ltgwMTYKEbG6sjyiuMFOol/zRk+2xrnklSSOmxNlG/72H0nXpRrJkZoHKq9nBID1r+GA5hbnu5d9YVEVa4ElSZL5G3bNrj1xcllVdHK9JmyNmAzFMsn2GpuFccS1Z6NlYnrSQBGpJESfGufoq1BY4kZO7OlHHbWZG+lGR7bZVCw6j5vmz9bl0LQOZKmRqKdY4/aVZKuXy211CkHo1tbEv1ZNttYkys7RXMUopYIeTNzjXFUurlTNo6sCyoogIwiFJjVh3+fKrON43ZbOyI4ZyWY5EQkm+l3KzK0sAFdZPeOW3NinUYIeTOnxXygtsLgGfrqQvUQbi6Cu/VH0o62pMNtIh5+UFolyRc1zxouuZ77AHraCLq9+xrlRRS+mgyZ09/jyPAUspPR9pVVFIuIzSQZKwh1O/cKofKJ1a9KOrLkULlIbKASAGIJBOk6H6wrIpRTUUn0DlZawZ66/eX9aKbhj1l8x+tFRNdgjpuGHqDzb4jV0uACTsASfIVQ4UeoPb8RqxikLIyjcqQPdR8mciqGZhna+LSwGCqj3CqkwrXCgISeUn2VIudWNtyrEKGV17Lo2oYe8VQ4VikS1iFdM4cWxlzhJyvO/a9wPs3q5g2e4zXXAUFVRFAhVRRACjuED86pp9mad17LxwrrMgGCAYMxmEr76rOhBmDpvpy7vOtJ8cM7RORljsrPYyhonWNdJ5mmvi1KMDmLFWWYEahQCADA7I/LWs7ZvSKaodiDtI0O3+KrXLTA9kwe4H8Q8Nq0G4kCzzJDEsgb6uh0BBlTLctImnvj1IcgHr5zGnVLIVyjw635Ci36Cl7MLEKQSGEH6wOn/KP1rl23rq8ffzuCJEKgE88qKhnv2/OuVYanzrXjJYlLRFKBWohBT6ZThQARSRThS0gEpIp1FIApaBS0FCUtEUsUAJFOFJSikBNY7Q8xRRZ3HnRWcl2UjpMAsLHn8Rq4Kgw66D2/EanFTZDQ18KjHMUUnvj9alWhKa29OxURXF/L9KjUxU78qqnl50mNIjvju8x50i3efI6HwNS3uzVPn5jWix0GKTn4+4/sa5pxqfM109vVde+PZXPlBJ8zVwexNFcU7LUoUdwpxQVrYqIctLlqZUFJFKwIwtOy08CnCiwIstGWpaQUgojy0uWpKIoKI4oipIooAjilAp9FAC29x50U5N/bRUspH//Z',
	'title':'Advanced Engineering Mathematics',
	'desc':'Author:Michael Greenberg Edition:2 Book Id:103'
	},
	{
	'url':'https://data-flair.training/blogs/wp-content/uploads/sites/2/2018/08/Python-in-a-nutshell-1.jpg',
	'title':'Python in a Nutshell',
	'desc':'Author:Alex Martell Edition:5 Book Id:104'
	},
	{
	'url':'https://images-na.ssl-images-amazon.com/images/I/91ctQaCi8QL.jpg',
	'title':'Computer Science with JAVA',
	'desc':'Author:Sumita Arora Edition:7 Book Id:105'
	},
	{
	'url':'https://images-na.ssl-images-amazon.com/images/I/515iDOTd0XL._SX373_BO1,204,203,200_.jpg',
	'title':'Data Structures & Algorithms using C',
	'desc':'Author:R.S.Salaria Edition:5 Book Id:106'	
	},
	{'url':'https://images-na.ssl-images-amazon.com/images/I/51HfkDbya7L._SX378_BO1,204,203,200_.jpg',
	'title':'HTML & CSS',
	'desc':'Author:Thomas A.Powell Edition:5 Book Id:107'
	},
	{
	'url':'https://mitpress.mit.edu/sites/default/files/styles/large_book_cover/http/mitp-content-server.mit.edu%3A18180/books/covers/cover/%3Fcollid%3Dbooks_covers_0%26isbn%3D9780262012119%26type%3D.jpg?itok=usynno1-',
	'title':'Introduction to Machine Learning',
	'desc':'Author:Ethem Alpaydin Edition:2 Book Id:108'
	},
	{
	'url':'https://images-na.ssl-images-amazon.com/images/I/51JYTR9QSTL.jpg',
	'title':'Artificial Intelligence: A Modern Approach',
	'desc':'Author:Stuart Russell and Peter Norvig Edition:2 Book Id:109'
	},
	{
	'url':'https://images-na.ssl-images-amazon.com/images/I/81chUd-wx0L.jpg',
	'title':'The C++ Programming Language',
	'desc':'Author:Bjarne Stroustrup Edition:3 Book Id:110'
	},
	{
	'url':'https://images-na.ssl-images-amazon.com/images/I/81mM7qbeXML.jpg',
	'title':'Object Oriented Programming with C++ and Java',
	'desc':'Author:E.Balagurusamy Edition:8 Book Id:111'
	}]
	return render_template('home.html',carddata=data)

@app.route('/login')
def login():
	return render_template('login.html')


if __name__=="__main__":    
	app.run(debug=True)