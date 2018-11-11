About
-----

With this app you can control multiple mpv players in one system.

Scheme
------
```
+------------------------------------------+
|  +------+                                |
|  | mpv1 |----+        Computer 1         |
|  +------+    |                           |
|              |                           |
|  +------+    |    +-----------------+    |   +---------+
|  | mpv2 |----+----| MPV HTTP Router |----|---| MPV Web |
|  +------+    |    +-----------------+\   |   +---------+
|              |                        |  |
|  +------+    |                        |  |   +-------------+
|  | mpv3 |----+                        |  |   |  MPVRemote  |
|  +------+                             +--|---|   +---------+
+------------------------------------------+   |   | MPV Web |
                                               +---+---------+
```

* MPV HTTP Router: https://github.com/voidpp/mpv-http-router
* MPV Web: https://github.com/voidpp/mpv-web
* MPVRemote: https://github.com/voidpp/MPVRemote

Install
-------

TODO
