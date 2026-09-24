from flask import Flask, request, jsonify, send_file
import qrcode
import os
import io

app = Flask(__name__)

QR_FOLDER = "generated_qr"
os.makedirs(QR_FOLDER, exist_ok=True)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "QRGen Microservice",
        "status": "running",
        "message": "QR Code Generator API is running"
    }), 200


@app.route("/api/qr", methods=["GET"])
def generate_qr():
    text = request.args.get("text", "").strip()
    size = request.args.get("size", "300")

    if not text:
        return jsonify({
            "success": False,
            "error": "Missing required parameter: text"
        }), 400

    try:
        size = int(size)
    except ValueError:
        return jsonify({
            "success": False,
            "error": "Size must be a valid integer"
        }), 400

    if size < 100 or size > 1000:
        return jsonify({
            "success": False,
            "error": "Size must be between 100 and 1000"
        }), 400

    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4
        )

        qr.add_data(text)
        qr.make(fit=True)

        image = qr.make_image(fill_color="black", back_color="white")
        image = image.resize((size, size))

        filename = "qr_code.png"
        filepath = os.path.join(QR_FOLDER, filename)
        image.save(filepath)

        return jsonify({
            "success": True,
            "message": "QR code generated successfully",
            "text": text,
            "size": size,
            "image_url": f"/api/qr/image?text={text}&size={size}"
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"QR generation failed: {str(e)}"
        }), 500


@app.route("/api/qr/image", methods=["GET"])
def qr_image():
    text = request.args.get("text", "").strip()
    size = request.args.get("size", "300")

    if not text:
        return jsonify({
            "success": False,
            "error": "Missing required parameter: text"
        }), 400

    try:
        size = int(size)
    except ValueError:
        return jsonify({
            "success": False,
            "error": "Size must be a valid integer"
        }), 400

    if size < 100 or size > 1000:
        return jsonify({
            "success": False,
            "error": "Size must be between 100 and 1000"
        }), 400

    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4
        )

        qr.add_data(text)
        qr.make(fit=True)

        image = qr.make_image(fill_color="black", back_color="white")
        image = image.resize((size, size))

        image_bytes = io.BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes.seek(0)

        return send_file(
            image_bytes,
            mimetype="image/png",
            download_name="qr_code.png"
        )

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"QR image generation failed: {str(e)}"
        }), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": "HTTP method not allowed"
    }), 405


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)