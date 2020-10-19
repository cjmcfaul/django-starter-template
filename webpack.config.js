const path                      = require('path');
const resolve                   = path.resolve.bind(path, __dirname);
const url                       = require('url');
const webpack                   = require('webpack');
const autoprefixer              = require('autoprefixer');
// Plugins
const { BundleAnalyzerPlugin }  = require('webpack-bundle-analyzer');
const BundleTracker             = require('webpack-bundle-tracker');
const MiniCssExtractPlugin      = require('mini-css-extract-plugin');
const { CleanWebpackPlugin }    = require('clean-webpack-plugin');
const StylelintPlugin           = require('stylelint-webpack-plugin');
// Custom vars
const distPath                  = resolve('./frontend/static');
const serverHost             = process.env.WEBPACK_SERVER_HOST || '0.0.0.0';
const serverPort             = process.env.WEBPACK_SERVER_PORT || '8080';
// https://github.com/owais/django-webpack-loader/blob/master/examples/hot-reload/webpack.config.js
const hotUrl              = url.resolve('http://'+serverHost+':'+serverPort, '/')

module.exports = (env, argv) => {
  const devMode = argv.mode !== 'production';
  const hotMode = argv.hot !== undefined;
  let plugins = [
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({
      filename: '[name].css',
      chunkFilename: '[name].css',
    }),
    new BundleTracker({
      indent: 2,
    }),
  ]
  if (env && env.analyze) {
    plugins = plugins.concat([new BundleAnalyzerPlugin()])
  }
  return {
    entry: {
      vendors: './frontend/src/vendors.js',
      main: {
        import: './frontend/src/main.js',
        dependOn: 'vendors'
      }
    },
    output: {
      filename: '[name].bundle.js',
      chunkFilename: '[name].chunk.js',
      path: distPath,
      publicPath: hotMode ? hotUrl : ''
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          loader: 'babel-loader'
        },
        {
          test: /\.scss$/,
          use: [
            MiniCssExtractPlugin.loader,
            {
              loader: 'css-loader',
              options: {
                'sourceMap': true
              }
            },
            {
              loader: 'postcss-loader',
              options: {
                'sourceMap': true,
                'plugins': function () {
                  return [autoprefixer];
                }
              }
            },
            'sass-loader',
          ]
        },
        {
          test: /\.(ttf|eot|svg|woff(2)?)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
          loader: "file-loader",
          options: {
            name: "[name].[ext]",
            outputPath: "fonts/",
          }
        },
        {
          test: /\.(png|jpg|gif|jpeg|)$/i,
          loader: 'file-loader',
          options: {
            name: "[name].[ext]",
            outputPath: "images/",
          },
        },
      ],
    },
    plugins: plugins,
    resolve: {
      alias: {
        '@': resolve('./frontend/src/'),
      },
      extensions: ['.ts', '.tsx', '.js', '.jsx']
    },
    devtool: 'cheap-source-map',
    devServer: {
      host: serverHost,
      port: serverPort,
      hot: hotMode,
      serveIndex: false,
      overlay: true,
      quiet: false,
      headers: { 'Access-Control-Allow-Origin': '*' }
    }
  };
};
