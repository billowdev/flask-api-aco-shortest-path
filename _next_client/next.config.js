/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ["localhost", 'fastly.picsum.photos', 'picsum.photos'],
  },
}

module.exports = nextConfig

